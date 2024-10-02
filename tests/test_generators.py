import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

"""
Тестирование функции filter_by_currency
"""


@pytest.mark.parametrize(
    "fixture_name, currency, expected_output",
    [
        (
            "transactions_input",
            "USD",
            [
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
            ],
        )
    ],
)
def test_filter_by_currency(request, fixture_name, currency, expected_output):
    input_list = request.getfixturevalue(fixture_name)
    gen_filter_by_currency = filter_by_currency(input_list, currency)
    assert next(gen_filter_by_currency) == expected_output[0]
    assert next(gen_filter_by_currency) == expected_output[1]


def test_filter_by_currency_no_such_currency(transactions_input, currency="EUR"):
    gen_filter_by_currency = filter_by_currency(transactions_input, currency)
    # assert next(gen_filter_by_currency) == expected_output
    with pytest.raises(StopIteration):
        next(gen_filter_by_currency)


def test_filter_by_currency_empty_input(transactions=[], currency="USD"):
    gen_filter_by_currency = filter_by_currency(transactions, currency)
    with pytest.raises(ValueError):
        next(gen_filter_by_currency)


"""
Тестирование функции transaction_descriptions
"""


def test_transaction_descriptions(transactions_input):
    descriptions = transaction_descriptions(transactions_input)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_empty_input(transactions=[]):
    descriptions = transaction_descriptions(transactions)
    with pytest.raises(ValueError):
        next(descriptions)


"""
Тестирование функции card_number_generator
"""


@pytest.mark.parametrize(
    "first_diap_test, last_diap_test, expected_output",
    [
        (
            110001,
            110005,
            [
                "0000 0000 0011 0001",
                "0000 0000 0011 0002",
                "0000 0000 0011 0003",
                "0000 0000 0011 0004",
                "0000 0000 0011 0005",
            ],
        )
    ],
)
def test_card_number_generator(first_diap_test, last_diap_test, expected_output):
    card_number_test = card_number_generator(first_diap_test, last_diap_test)
    i = 0
    for _ in range(first_diap_test, last_diap_test + 1):
        assert next(card_number_test) == expected_output[i]
        i += 1


def test_card_number_generator_range_exceeded(first_diap_test=1, last_diap_test=5):
    card_number_test = card_number_generator(first_diap_test, last_diap_test)
    with pytest.raises(StopIteration):
        next(card_number_test)
        next(card_number_test)
        next(card_number_test)
        next(card_number_test)
        next(card_number_test)
        next(card_number_test)


def test_card_number_generator_17digits(first_diap_test=1, last_diap_test=12345678901234567):
    card_number_test = card_number_generator(first_diap_test, last_diap_test)
    with pytest.raises(ValueError):
        next(card_number_test)


def test_card_number_generator_not_integer(first_diap_test=1, last_diap_test="5"):
    card_number_test = card_number_generator(first_diap_test, last_diap_test)
    with pytest.raises(ValueError):
        next(card_number_test)


def test_card_number_generator_max_first(first_diap_test=5, last_diap_test=2):
    card_number_test = card_number_generator(first_diap_test, last_diap_test)
    with pytest.raises(ValueError):
        next(card_number_test)
