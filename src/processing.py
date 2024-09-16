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


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
