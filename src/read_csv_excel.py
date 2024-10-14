import logging
from pathlib import Path
from typing import Dict, List

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
file_path_log = BASE_DIR / "logs" / "read_csv_excel.log"

logger = logging.getLogger("read_csv_excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{file_path_log}", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_from_csv(file_path: Path) -> List[Dict]:
    """Функция считывает финансовые операций из CSV файла и выдает список словарей с транзакциями."""
    try:
        logger.debug(f"Чтение данных из файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = pd.read_csv(file, delimiter=";")
        logger.info(f"Данные из файла {file_path} получены")
        return transactions.to_dict(orient="records")
    except FileNotFoundError as ex:
        logger.error(f"Ошибка: {ex} - файл {file_path} не найден")
        return []


def get_transactions_from_excel(file_path: Path) -> List[Dict]:
    """Функция считывает финансовые операций из Excel файла и выдает список словарей с транзакциями."""
    try:
        logger.debug(f"Чтение данных из файла {file_path}")
        with open(file_path, "rb") as file:
            transactions = pd.read_excel(file)
        logger.info(f"Данные из файла {file_path} получены")
        return transactions.to_dict(orient="records")
    except FileNotFoundError as ex:
        logger.error(f"Ошибка: {ex} - файл {file_path} не найден")
        return []


# if __name__ == '__main__':
#
#     file_path_csv = BASE_DIR / 'data' / 'transactions.csv'
#     file_path_excel = BASE_DIR / 'data' / 'transactions_excel.xlsx'
#
#     print(get_transactions_from_csv(file_path_csv))
#     print(get_transactions_from_excel(file_path_excel))
