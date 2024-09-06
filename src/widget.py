from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_input: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счета"""
    masked_number = str()
    if "Maestro" in card_input or "MasterCard" in card_input or "Visa" in card_input:
        masked_number = card_input[:-16] + get_mask_card_number(card_input[-16:])
    elif "Счет" in card_input:
        masked_number = card_input[:-20] + get_mask_account(card_input[-20:])
    else:
        print("Введите корректное обозначение типа карты или Счет")
    return masked_number


def get_date(date_time: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    decoded_datetime = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
    converted_date = decoded_datetime.strftime("%d.%m.%Y")
    return converted_date


if __name__ == "__main__":
    print(mask_account_card(input("Insert your card or account: ")))
    print(get_date(input("Insert date and time: ")))
