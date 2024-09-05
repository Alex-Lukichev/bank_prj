from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(card_or_acc_number: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счета"""
    # masked_number = str()
    number_list = card_or_acc_number.split()

    if number_list[0] in ['Maestro', 'MasterCard', 'Visa']:
        number_list[-1] = get_mask_card_number(number_list[-1])
    elif number_list[0] in ['Счет']:
        number_list[-1] = get_mask_account(number_list[-1])
    else:
        print('Введите корректное обозначение типа карты или Счет')
    return ' '.join(number_list)


if __name__ == '__main__':
    print(mask_account_card(input("Insert your card or account: ")))
