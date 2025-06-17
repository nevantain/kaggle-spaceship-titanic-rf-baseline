#!/usr/bin/env python3
"""Spaceship Titanic Kaggle solution script.

This script trains a simple RandomForest model and prepares a submission file.
It can be executed from the command line:

    python solution.py --train path/to/train.csv --test path/to/test.csv --output result.csv

If no arguments are supplied it defaults to the files located in the working
folder.
"""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CATEGORICAL_SPLIT_COL = "Cabin"
SPLIT_PARTS = ["Deck", "Num", "Side"]
DROP_COLS_COMMON = ["Destination", "Name", "PassengerId", "VIP", "HomePlanet"]
RANDOM_STATE = 42


# ---------------------------------------------------------------------------
# Processing helpers
# ---------------------------------------------------------------------------

def _split_cabin(df: pd.DataFrame) -> pd.DataFrame:
    """Split *Cabin* column into *Deck*, *Num*, and *Side* and drop original."""
    df[SPLIT_PARTS] = df[CATEGORICAL_SPLIT_COL].str.split("/", expand=True)
    return df.drop(columns=[CATEGORICAL_SPLIT_COL])


def _prepare_features(
    df: pd.DataFrame,
    encoder: OrdinalEncoder,
    fit_encoder: bool = False,
) -> pd.DataFrame:
    """Return dataframe with engineered features ready for modeling."""

    df = _split_cabin(df.copy())

    # Keep numeric "Num" as float
    df["Num"] = pd.to_numeric(df["Num"], errors="coerce").fillna(-1)

    # Drop target and meta columns from features
    feature_df = df.drop(columns=DROP_COLS_COMMON + ["Transported"], errors="ignore")

    # Fit / transform encoder on *Deck* and *Side*
    if fit_encoder:
        encoder.fit(feature_df[["Deck", "Side"]])
    feature_df[["Deck", "Side"]] = encoder.transform(feature_df[["Deck", "Side"]])

    return feature_df


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(train_csv: Path, test_csv: Path, output_csv: Path) -> None:
    """Train model and create submission file."""

    train = pd.read_csv(train_csv)
    test = pd.read_csv(test_csv)

    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)

    X_train = _prepare_features(train, encoder=encoder, fit_encoder=True)
    y_train = train["Transported"]

    X_test = _prepare_features(test, encoder=encoder, fit_encoder=False)

    model = RandomForestClassifier(random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    submission = pd.DataFrame({
        "PassengerId": test["PassengerId"],
        "Transported": preds,
    })
    submission.to_csv(output_csv, index=False)
    print(f"Submission file saved to {output_csv.resolve()}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train RandomForest model for Kaggle Spaceship Titanic competition and create submission file.",
    )
    parser.add_argument("--train", default="train.csv", type=Path, help="Path to train CSV file.")
    parser.add_argument("--test", default="test.csv", type=Path, help="Path to test CSV file.")
    parser.add_argument("--output", default="result.csv", type=Path, help="Output submission CSV path.")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    run(args.train, args.test, args.output)


if __name__ == "__main__":
    main()