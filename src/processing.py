from typing import List

from src.widget import get_date

""" 
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Пример входных данных
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
"""


def filter_by_state(list_of_dict: List[dict], state_value: str ='EXECUTED') -> List[dict]:
    """ Функция возвращает список словарей, отфильтрованный по заданному параметру state. """
    filtered_list = list()
    for el in list_of_dict:
        if el['state'] == state_value:
            filtered_list.append(el)
    return filtered_list


"""
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
"""
def sort_by_date(list_of_dict: List[dict], sort_order: bool = True) -> List[dict]:
    """ Функция сортирует список словарей по дате, параметр по умолчанию - по убыванию. """
    sorted_list = sorted(list_of_dict, key=lambda x: x[get_date('date')], reverse = sort_order)
    return sorted_list
