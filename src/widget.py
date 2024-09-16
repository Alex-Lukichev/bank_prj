from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_input: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счета"""
    masked_number = str()
    if "Maestro" in card_input or "MasterCard" in card_input or "Visa" in card_input:
        if any(not char.isalpha() and not char.isspace() for char in card_input[:-16]):
            raise ValueError("Длина номера карты больше 16 или тип карты имеет некорректные символы")
        else:
            masked_number = card_input[:-16] + get_mask_card_number(card_input[-16:])
    elif "Счет" in card_input:
        if any(not char.isalpha() and not char.isspace() for char in card_input[:-20]):
            raise ValueError("Длина номера счета больше 20 или тип Счет имеет некорректные символы")
        else:
            masked_number = card_input[:-20] + get_mask_account(card_input[-20:])
    else:
        raise ValueError("корректное обозначение типа карты или типа Счет")
    return masked_number


def get_date(date_time: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    if date_time == "":
        raise ValueError("Получен пустой ввод")

    try:
        decoded_datetime = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        raise ValueError("Формат 'дата-время' на входе некорректный, ожидаемый формат: YYYY-MM-DDTHH:MM:SS.ssssss")

    converted_date = decoded_datetime.strftime("%d.%m.%Y")
    return converted_date


if __name__ == "__main__":
    print(mask_account_card(input("Insert your card or account: ")))
    print(get_date(input("Insert date and time: ")))
