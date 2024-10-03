import json


def read_operations(path: str) -> list:
    """Получение списка словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
                if isinstance(operations_data, list):
                    return operations_data
                else:
                    return []
            except (json.JSONDecodeError, IOError):
                return []
    except FileNotFoundError:
        return []


# if __name__ == '__main__':
#     transactions = read_operations('data/operations.json')
#     print(transactions)
