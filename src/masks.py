import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX."""
    logger.debug("Получен номер карты")
    if not card_num.isdigit():
        logger.error("Validation Error: Номер карты имеет нечисловые символы или пробелы")
        raise ValueError("Номер карты имеет нечисловые символы или пробелы")
    if len(card_num) != 16:
        logger.error(f"Validation Error: Некорректная длина номера карты ({len(card_num)} вместо 16).")
        raise ValueError("Длина номера карты не равна 16")
    masked_card_num = card_num[0:4] + " " + card_num[4:6] + "** **** " + card_num[12:]
    logger.debug(f"Маска номера карты: {masked_card_num}")
    logger.info("Маска номера карты сгенерирована успешно")
    return masked_card_num


def get_mask_account(account_num: str) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    logger.debug("Получен номер счета")
    if not account_num.isdigit():
        logger.error("Validation Error: Номер счета имеет нечисловые символы или пробелы")
        raise ValueError("Номер счета имеет нечисловые символы или пробелы")
    if len(account_num) != 20:
        logger.error(f"Validation Error: Некорректная длина номера счета ({len(account_num)} вместо 20).")
        raise ValueError("Длина номера счета не равна 20")
    masked_account_num = "**" + account_num[-4:]
    logger.debug(f"Маска номера счета: {masked_account_num}")
    logger.info("Маска номера счета сгенерирована успешно")
    return masked_account_num


# if __name__ == "__main__":
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_account("73654108430135874305"))
