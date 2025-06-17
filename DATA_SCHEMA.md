# Схема данных Spaceship Titanic (RU)

Ниже представлена структура исходных файлов `train.csv` / `test.csv`.

Ниже представлена **структура** оригинальных файлов `train.csv` / `test.csv` Kaggle.
  
Реальные данные соревнования не включены — только названия столбцов, ожидаемые типы и краткое описание.  
Столбец `Transported` присутствует **только** в `train.csv` (целевая переменная).

Колонка `Transported` присутствует **только** в `train.csv` (это целевая переменная).

| Column          | Type      | Example value | Description                                         |
|-----------------|-----------|---------------|-----------------------------------------------------|
| PassengerId     | string    | `0001_01`     | Уникальный идентификатор пассажира ("группа_индекс").|
| HomePlanet      | category  | `Earth`       | Планета, с которой пассажир вылетел.               |
| CryoSleep       | boolean   | `True`        | Находился ли пассажир в состоянии криосна.         |
| Cabin           | string    | `B/0/P`       | Составная каюта (`Палуба/Номер/Сторона`).           |
| Destination     | category  | `TRAPPIST-1e` | Планета назначения.                                 |
| Age             | int/float | `27`          | Возраст пассажира.                                 |
| VIP             | boolean   | `False`       | Является ли пассажир VIP-персоной.                  |
| RoomService     | float     | `0`           | Сумма, потраченная на обслуживание в номере.       |
| FoodCourt       | float     | `2725`        | Сумма, потраченная в фудкорте.                      |
| ShoppingMall    | float     | `0`           | Сумма, потраченная в магазине.                      |
| Spa             | float     | `0`           | Сумма, потраченная на сауны.                        |
| VRDeck          | float     | `0`           | Сумма, потраченная на VR-палубу.                    |
| Name            | string    | `Sandie Deckow`| Полное имя пассажира.                               |
| Transported     | boolean   | `True`        | Целевая переменная: был ли пассажир переведен в другую измерение? *(train only)* |

### Минимальный пример CSV (заголовок + 1 синтетическая строка)

```csv
PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported
0001_01,Earth,False,B/0/P,TRAPPIST-1e,27,False,0,2725,0,0,0,"Sandie Deckow",True
```

Вы можете создать такой тестовый файл локально для быстрых проверок, но **не выкладывайте** реальные данные Kaggle в открытый репозиторий.

---

# Spaceship Titanic Data Schema (EN)

Below is the structure of the original `train.csv` / `test.csv` files. No real competition data is included — only column names, expected dtypes and brief meaning.
`Transported` exists **only** in `train.csv` (target variable).

| Column          | Type      | Example value | Description                                         |
|-----------------|-----------|---------------|-----------------------------------------------------|
| PassengerId     | string    | `0001_01`     | Unique passenger identifier *("group_index")*.     |
| HomePlanet      | category  | `Earth`       | Planet where the passenger embarked.               |
| CryoSleep       | boolean   | `True`        | Whether passenger was in cryo-sleep.               |
| Cabin           | string    | `B/0/P`       | Composite cabin (`Deck/Num/Side`).                 |
| Destination     | category  | `TRAPPIST-1e` | Destination planet.                                |
| Age             | int/float | `27`          | Passenger age.                                     |
| VIP             | boolean   | `False`       | Whether passenger is VIP.                          |
| RoomService     | float     | `0`           | Amount spent on room service.                      |
| FoodCourt       | float     | `2725`        | Amount spent in the food court.                    |
| ShoppingMall    | float     | `0`           | Amount spent in the shopping mall.                 |
| Spa             | float     | `0`           | Amount spent at the spa.                           |
| VRDeck          | float     | `0`           | Amount spent on the VR deck.                       |
| Name            | string    | `Sandie Deckow` | Passenger full name.                            |
| Transported     | boolean   | `True`        | Target: was passenger transported to another dimension? *(train only)* |

## Minimal dummy CSV example

```csv
PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported
0001_01,Earth,False,B/0/P,TRAPPIST-1e,27,False,0,2725,0,0,0,"Sandie Deckow",True
```

Feel free to create such a dummy file locally for quick tests; do **not** commit the real Kaggle data files into the repository.
