from datetime import datetime
from typing import List


def filter_by_state(list_of_dict: List[dict], state_value: str = "EXECUTED") -> List[dict]:
    """Функция возвращает список словарей, отфильтрованный по заданному параметру state."""
    filtered_list = list()
    for el in list_of_dict:
        if el["state"] == state_value:
            filtered_list.append(el)
    return filtered_list


def sort_by_date(list_of_dict: List[dict], sort_order: bool = True) -> List[dict]:
    """Функция сортирует список словарей по дате, параметр по умолчанию - по убыванию."""
    try:
        sorted_list = sorted(list_of_dict, key=lambda x: datetime.fromisoformat(x["date"]), reverse=sort_order)
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")
    return sorted_list


def json_transactions_reformat(transactions: List[dict]) -> List[dict]:
    # Функция переформатирует список словарей со структурой данных из JSON-файла в структуру данных CSV и Excel-файлов.
    new_transactions = []
    for transaction in transactions:
        if not transaction:
            continue
        new_dict = {
            'id': transaction.get('id'),
            'state': transaction.get('state'),
            'date': transaction.get('date'),
            'amount': transaction.get('operationAmount', {}).get('amount', ''),
            'currency_name': transaction.get('operationAmount', {}).get('currency', {}).get('name', ''),
            'currency_code': transaction.get('operationAmount', {}).get('currency', {}).get('code', ''),
            'from': transaction.get('from', ''),
            'to': transaction.get('to', ''),
            'description': transaction.get('description', '')
        }
        new_transactions.append(new_dict)
    return new_transactions

def filter_transactions_by_currency(transactions: List[dict], currency_code: str = 'RUB') -> List[dict]:
        # Функция возвращает список словарей, отфильтрованный по валюте; валюта по умолчанию 'RUB'.
    filtered_transactions = [t for t in transactions if t.get('currency_code') == currency_code]
    return filtered_transactions

# if __name__ == "__main__":
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
#     print(
#         sort_by_date(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
