import json
import os

""" Вариант 1 """
def read_operations(path: str) -> list:
    """ Получение списка словарей с данными о финансовых транзакциях """
    try:
        with open(path, 'r', encoding='utf-8') as file:
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


# """ Вариант 2 """
# def read_operations_2(file_path):
#     """ Получение списка словарей с данными о финансовых транзакциях """
#     try:
#         if not os.path.exists(file_path):
#             return []
#         with open(file_path, 'r',encoding='utf-8') as file:
#             data = json.load(file)
#             if isinstance(data, list):
#                 return data
#             else:
#                 return []
#     except (json.JSONDecodeError, IOError):
#         return []




if __name__ == '__main__':
    transactions = read_operations('data/operations.json')
    print(transactions)







# def get_operations(path: str, city: str) -> bool:
#     """ Получение средней температуры """
#     try:
#         with open(path) as city_file:
#             try:
#                 city_data = json.load(city_file)
#             except json.JSONDecodeError:
#                 print('Ошибка декодирования файла')
#                 return False
#     except FileNotFoundError:
#         print('Файл не найден')
#         return False
#
#     # print(city_data)
#
#     avg_temp = round(sum(city_data[city].values()) / len(city_data[city].keys()), 2)
#     # print(avg_temp)
#     out_data = {
#         city: {
#             "Average temperature": avg_temp
#         }
#     }
#     with open('src/out.json', 'w') as out_file:
#         json.dump(out_data, out_file)
#
#     return True
#
# if __name__ == '__main__':
#     get_avg_for_city('src/data.json', 'Moscow')
#
#
#
#
# def stat_decorator(func):
#     """Декоратор для вывода статистики по отфильтрованным транзакциям."""
#
#     def wrapper(*args, **kwargs):
#         filtered_transactions = func(*args, **kwargs)
#         total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
#         print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
#         return filtered_transactions
#
#     return wrapper
#
# @stat_decorator
# def filter_transactions_by_currency(input_file, output_file, currency):
#     """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""
#
#     with open(input_file, 'r') as f:
#         transactions = json.load(f)
#
#     filtered_transactions = [transaction for transaction in transactions if transaction['currency'] == currency]
#
#     with open(output_file, 'w') as f:
#         json.dump(filtered_transactions, f, indent=4)
#
#     return filtered_transactions
#
# def main():
#     input_file = 'transactions.json'
#     output_file = 'transactions_filtered.json'
#     currency = 'USD'
#
#     filtered_transactions = filter_transactions_by_currency(input_file, output_file, currency)
#     print(filtered_transactions)
