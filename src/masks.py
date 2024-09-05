def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX."""
    return card_num[0:4] + " " + card_num[4:6] + "** **** " + card_num[12:]


def get_mask_account(account_num: str) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    return "**" + account_num[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
