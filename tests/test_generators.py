import  pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

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
                    "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                    "name": "USD",
                    "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"
                }
            ]
        )
    ]
)
def test_filter_by_currency(request, fixture_name, currency, expected_output):
    input_list = request.getfixturevalue(fixture_name)
    gen_filter_by_currency = filter_by_currency(input_list, currency)
    assert next(gen_filter_by_currency) == expected_output[0]
    assert next(gen_filter_by_currency) == expected_output[1]


def test_filter_by_currency_no_more_record(transactions_input, currency="USD"):
    gen_filter_by_currency = filter_by_currency(transactions_input, currency)
    with pytest.raises(StopIteration):
        next(gen_filter_by_currency)
        next(gen_filter_by_currency)
        next(gen_filter_by_currency)
        next(gen_filter_by_currency)


def test_transaction_descriptions(transactions_input):
    descriptions = transaction_descriptions(transactions_input)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"



# def test_card_number_generator():
#
#     pass


