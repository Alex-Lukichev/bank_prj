import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_input, masked_number", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                       ("Счет 64686473678894779589", "Счет **9589"),
                                                       (
                                                       "MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                       ("Счет 35383033474447895560", "Счет **5560"),
                                                       ("Visa Classic 6831982476737658",
                                                        "Visa Classic 6831 98** **** 7658"),
                                                       ("Visa Platinum 8990922113665229",
                                                        "Visa Platinum 8990 92** **** 5229"),
                                                       ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                       ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(card_input, masked_number):
    assert mask_account_card(card_input) == masked_number


def test_mask_account_card_nonstandard_length():
    with pytest.raises(ValueError):
        mask_account_card("Maestro 15968378687051999")


def test_mask_account_card_incorrect_cardname():
    with pytest.raises(ValueError):
        mask_account_card("Unionpay 7158300734726758")


def test_mask_account_card_wrong_symbols():
    with pytest.raises(ValueError):
        mask_account_card("Счет:73654108430135874305")


def test_mask_account_card_spaces():
    with pytest.raises(ValueError):
        mask_account_card("Visa Classic 6831 9824 7673 7658")


def test_get_date(date_input):
    assert get_date(date_input) == "11.03.2024"


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_incorrect_format():
    with pytest.raises(ValueError):
        get_date("2024-03-11 02:26:18.671407")