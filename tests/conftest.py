import pytest


@pytest.fixture
def date_input():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def list_transactions1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_transactions2():
    return [
        {"id": 112233445, "state": "CANCELED", "date": "2021-01-30T18:35:29.512364"},
        {"id": 343455333, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 322211344, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 666555443, "state": "CANCELED", "date": "2018-09-12T21:30:00.241689"},
    ]


@pytest.fixture
def list_transactions_same_state():
    return [
        {"id": 11111, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 22222, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 33333, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 44444, "state": "EXECUTED", "date": "2018-09-12T21:30:00.241689"},
    ]


@pytest.fixture
def list_transactions_invalid_dates():
    return [
        {"id": 123456789, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 987654321, "state": "CANCELED", "date": "2019/07/03"},  # Некорректный формат
        {"id": 112233445, "state": "EXECUTED", "date": "2019-13-03T18:35:29.512364"},  # Некорректный месяц
        {"id": 998877665, "state": "EXECUTED", "date": "invalid-date"},  # Некорректный формат
        {"id": 778899001, "state": "CANCELED", "date": ""},  # Нет даты
    ]
