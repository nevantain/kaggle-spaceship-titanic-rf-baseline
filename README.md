# Spaceship Titanic — RandomForest Baseline

Это репозиторий с простым, но чистым **baseline-решением** для соревнования Kaggle [*Spaceship Titanic*](https://www.kaggle.com/competitions/spaceship-titanic).

Скрипт `solution.py`:
* Загружает `train.csv` и `test.csv`;
* Делит колонку `Cabin` на `Deck`, `Num`, `Side`;
* Кодирует категориальные признаки `Deck` и `Side` через `OrdinalEncoder` (c явной обработкой неизвестных категорий);
* Обучает `RandomForestClassifier` с фиксированным `random_state=42`;
* Предсказывает `Transported` для тестового набора и сохраняет `result.csv` в формате submission.

## Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # см. файл requirements.txt
```

Минимальный набор библиотек (Python >=3.9):

* pandas
* scikit-learn

## Использование

В каталоге, где лежат `train.csv` и `test.csv`:

```bash
python solution.py                   # сохранит result.csv
```

Или указать пути явно:

```bash
python solution.py \
    --train /path/to/train.csv \
    --test  /path/to/test.csv  \
    --output submission.csv
```

После выполнения появится файл `submission.csv`, который можно загружать на Kaggle.

### Флаги командной строки

| Флаг | По умолчанию | Описание |
|------|--------------|----------|
| `--train` | `train.csv` | Путь к файлу обучающей выборки |
| `--test`  | `test.csv`  | Путь к тестовому набору |
| `--output`| `result.csv`| Путь, куда сохранить файл submission |


## Структура проекта

```
├── solution.py      # основной скрипт
├── README.md        # вы читаете его
├── requirements.txt # список зависимостей (pip freeze)
├── train.csv        # данные Kaggle (не добавлять в публичный репозиторий!)
├── test.csv         # данные Kaggle (не добавлять в публичный репозиторий!)
└── result.csv       # пример получившегося submission
```

> **Важно ⚠️**: `train.csv`, `test.csv` и другие файлы датасета нарушают правила Kaggle при публичном распространении. Не загружайте их в открытый GitHub-репозиторий. Добавьте их в `.gitignore` или держите в приватном репо.

## Лицензия

Исходный код распространяется под лицензией MIT — см. файл `LICENSE`.

---

# Spaceship Titanic — RandomForest Baseline (EN)

This repository contains a simple but clean **baseline solution** for the Kaggle competition [*Spaceship Titanic*](https://www.kaggle.com/competitions/spaceship-titanic).

## Quick start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python solution.py --output result.csv
```

## Usage

```bash
# Default: expects train.csv & test.csv in working dir
python solution.py

# Custom paths
python solution.py \
    --train /path/to/train.csv \
    --test  /path/to/test.csv  \
    --output submission.csv
```

## Command-line flags

| Flag | Default | Description |
|------|---------|-------------|
| `--train` | `train.csv` | Path to training CSV |
| `--test`  | `test.csv`  | Path to test CSV |
| `--output`| `result.csv`| Where to save the submission |

## What the script does

1. Loads `train.csv` and `test.csv`.
2. Splits the `Cabin` column into `Deck`, `Num`, `Side`.
3. Encodes categorical features (`Deck`, `Side`) with `OrdinalEncoder` (handles unseen categories).
4. Trains `RandomForestClassifier` with `random_state=42`.
5. Predicts `Transported` for the test set and writes a submission file.

## Project structure

Note: **Kaggle data files (train.csv, test.csv, etc.) are subject to the competition rules – do NOT push them to a public GitHub repo.** Add them to `.gitignore` or keep the repository private.

## License

MIT — see `LICENSE` file.

