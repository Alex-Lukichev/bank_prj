def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX."""
    if not card_num.isdigit():
        raise ValueError("Номер карты имеет нечисловые символы или пробелы")
    if len(card_num) != 16:
        raise ValueError("Длина номера карты не равна 16")
    return card_num[0:4] + " " + card_num[4:6] + "** **** " + card_num[12:]


def get_mask_account(account_num: str) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    if not account_num.isdigit():
        raise ValueError("Номер счета имеет нечисловые символы или пробелы")
    if len(account_num) != 20:
        raise ValueError("Длина номера счета не равна 20")
    return "**" + account_num[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
