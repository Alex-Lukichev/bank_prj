import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_operations(path: str) -> list:
    """Получение списка словарей с данными о финансовых транзакциях"""
    try:
        logger.debug(f"Чтение данных из файла {path}")
        with open(path, "r", encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
                if isinstance(operations_data, list):
                    logger.info(f"Данные из файла {path} получены")
                    return operations_data
                else:
                    logger.warning(f"Данные из файла {path} - не список")
                    return []
            except (json.JSONDecodeError, IOError) as ex:
                logger.error(f"Произошла ошибка чтения файла: {ex}")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Ошибка: {ex} - файл {path} не найден")
        return []


# if __name__ == '__main__':
#     transactions = read_operations('data/operations.json')
#     print(transactions)
