import math
from pathlib import Path
from typing import Tuple
import re

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, json_transactions_reformat, filter_transactions_by_currency
from src.read_csv_excel import get_transactions_from_csv, get_transactions_from_excel
from src.utils import read_operations
from src.widget import get_date, mask_account_card

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
file_path_json = BASE_DIR / 'data' / 'operations.json'
file_path_csv = BASE_DIR / 'data' / 'transactions.csv'
file_path_xlsx = BASE_DIR / 'data' / 'transactions_excel.xlsx'


def main():
    """ Главная функция: чтение файла, фильтрация и вывод списка транзакций """
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')

    """ Выбор пользователем пункта меню о входном файле для получения транзакций. """
    menu_items = {1: 'JSON', 2: 'CSV', 3: 'XLSX'}
    print('Выберите необходимый пункт меню:')
    for key, value in menu_items.items():
        print(f'{key}. Получить информацию о транзакциях из {value}-файла')
    choice = int(input('\n'))
    print()
    if choice not in menu_items.keys():
        print('Некорректный ввод. Начните сначала.')
        raise ValueError('Некорректный выбор пункта меню')
    print(f'Для обработки выбран {menu_items[choice]}-файл.\n')
    if menu_items[choice] == 'JSON':
        transaction_list = read_operations(file_path_json)
        transaction_list = json_transactions_reformat(transaction_list)
    elif menu_items[choice] == 'CSV':
        transaction_list = get_transactions_from_csv(file_path_csv)
    elif menu_items[choice] == 'XLSX':
        transaction_list = get_transactions_from_excel(file_path_xlsx)
    # print(transaction_list) #test

    """ Выбор статуса интересующих пользователя операций. """
    statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print(
            'Введите статус, по которому необходимо выполнить фильтрацию.\n'
            f'Доступные для фильтровки статусы: {(', '.join(statuses))}\n'
        )
        user_input_state = input()
        print()
        filter_state = user_input_state.upper()
        if filter_state in statuses:
            print(f'Операции отфильтрованы по статусу "{filter_state}"\n')
            break
        else:
            print(f'Статус операции "{user_input_state}" недоступен.\n')

    transaction_list = filter_by_state(transaction_list, filter_state)
    # print(transaction_list) #test

    """ Получение от пользователя статуса сортировки операций по дате. """
    while True:
        sort_date_input = input('Отсортировать операции по дате? Да/Нет\n\n')
        print()
        sort_date_input_lower = sort_date_input.lower()
        if sort_date_input_lower == 'да':
            while True:
                ascending_input = input('Отсортировать по возрастанию или по убыванию?\n\n')
                print()
                ascending_input_lower = ascending_input.lower()
                if ascending_input_lower == 'по возрастанию':
                    transaction_list = sort_by_date(transaction_list, False)
                    break
                elif ascending_input_lower == 'по убыванию':
                    transaction_list = sort_by_date(transaction_list, True)
                    break
                else:
                    print(f'Параметр сортировки "{ascending_input}" недоступен.\n')
            break
        elif sort_date_input_lower == 'нет':
            break
        else:
            print(f'Параметр сортировки "{sort_date_input}" недоступен.\n')
    # print(transaction_list)  # test

    """ Получение от пользователя статуса вывода только рублевых транзакций. """
    while True:
        rub_input = input('Выводить только рублевые транзакции? Да/Нет\n\n')
        print()
        rub_input_lower = rub_input.lower()
        if rub_input_lower == 'да':
            transaction_list = filter_transactions_by_currency(transaction_list)
            break
        elif rub_input_lower == 'нет':
            break
        else:
            print(f'Параметр фильтрации "{rub_input}" недоступен.\n')

    # print(transaction_list)  # test

    """ Получение от пользователя статуса фильтрации списка транзакций по определенному слову. """
    while True:
        filtering_by_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n\n')
        print()
        filtering_by_word_lower = filtering_by_word.lower()
        if filtering_by_word_lower == 'да':
            word_for_filter = input('Введите слово для фильтрации:\n\n')
            pattern = re.compile(rf'\b{re.escape(word_for_filter)}\b', re.IGNORECASE)
            transaction_list = [t for t in transaction_list if pattern.search(t.get('description', ''))]
            break
        elif filtering_by_word_lower == 'нет':
            break
        else:
            print(f'Параметр фильтрации "{filtering_by_word}" недоступен.\n')
    # print(transaction_list)  # test

    """ Вывод итогового списка транзакций... """
    print('\nРаспечатываю итоговый список транзакций...\n')
    if transaction_list:
        print(f'Всего банковских операций в выборке: {len(transaction_list)}\n')
        for transaction in transaction_list:
            final_tr = []
            final_tr.append(f"{get_date(transaction['date'])} {transaction['description']}")
            from_account = transaction.get('from')
            to_account = transaction.get('to')
            if from_account and not (isinstance(from_account, float) and math.isnan(from_account)) and to_account:
                masked_from = mask_account_card(transaction['from'])
                masked_to = mask_account_card(transaction['to'])
                final_tr.append(f'{masked_from} -> {masked_to}')
            elif transaction['to']:
                masked_to = mask_account_card(transaction['to'])
                final_tr.append(masked_to)
            final_tr.append(f"Сумма: {transaction['amount']} {transaction['currency_name']}")
            print('\n'.join(final_tr), '\n')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

if __name__ == '__main__':
    main()
