from pathlib import Path
import logging

from collections import defaultdict, Counter

from read_csv_excel import get_transactions_from_csv, get_transactions_from_excel
from utils import read_operations

import re
from typing import List, Dict


BASE_DIR = Path(__file__).resolve().parent.parent
file_path_log = BASE_DIR / "logs" / "search_func.log"

logger = logging.getLogger("search_func")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{file_path_log}", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



def get_search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """ Функция возвращает список словарей, у которых в описании есть переданная строка поиска. """
    search_result = []

    for transaction in transactions:
        if transaction.get('description'):
            logger.debug(f"get_search_transactions: Проверка записи, имеющей id '{transaction.get('id')}'")
            try:
                match = re.search(search_str, transaction['description'], flags=re.IGNORECASE)
                if match:
                    logger.debug(f"get_search_transactions: Запись id '{transaction['id']}' "
                                 f"соответствует поисковой строке '{search_str}'")
                    search_result.append(transaction)
            except Exception as e:
                logger.error(f"get_search_transactions: Исключение обработки '{e}' записи id '{transaction.get('id')}'")

        else:
            logger.error(f"get_search_transactions: Для записи id: {transaction.get('id')} отсутствует 'description'")

    return  search_result


def get_transactions_count(transactions: List[Dict], categories: list) -> dict:
    """ Функция возвращает словарь {'название категории': 'количество операций в категории'}. """
    lowercase_categories = [el.lower() for el in categories]
    descriptions = []

    for transaction in transactions:
        if transaction.get('description'):
            logger.debug(f"get_transactions_count: Проверка записи, имеющей id: {transaction.get('id')}")
            try:
                if transaction['description'].lower() in lowercase_categories:
                    logger.debug(f"get_transactions_count: Запись id : {transaction['id']} "
                                 f"соответствует категории '{transaction['description']}' "
                                 f"в списке категорий {categories}")
                    descriptions.append(transaction['description'])
            except Exception as e:
                logger.error(f"get_transactions_count: Исключение обработки {e} записи id: {transaction.get('id')}")

        else:
            logger.error(f"get_transactions_count: Для записи id: {transaction.get('id')} отсутствует 'description'")

    description_counter = Counter(descriptions)
    return dict(description_counter)




if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent.parent

    file_path_csv = BASE_DIR / 'data' / 'transactions.csv'
    file_path_excel = BASE_DIR / 'data' / 'transactions_excel.xlsx'
    file_path_json = BASE_DIR / 'data' / 'operations.json'

    transactions = get_transactions_from_csv(file_path_csv)
    # transactions = get_transactions_from_excel(file_path_excel)
    # transactions = read_operations(file_path_json)
    print(get_search_transactions(transactions, 'организации'))
    # print(get_transactions_count(transactions, ["Открытие вклада", "Перевод организации", "Тестовая категория"]))


