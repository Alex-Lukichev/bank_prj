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


@pytest.fixture
def transactions_input():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions
