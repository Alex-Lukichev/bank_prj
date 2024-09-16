import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_user_input, masked_card_num",
    [("7000792289606361", "7000 79** **** 6361"), ("5443688377666600", "5443 68** **** 6600")],
)
def test_get_mask_card_number(card_user_input, masked_card_num):
    assert get_mask_card_number(card_user_input) == masked_card_num


@pytest.mark.parametrize(
    "acc_user_input, masked_acc_num", [("73654108430135874305", "**4305"), ("10012354220012781000", "**1000")]
)
def test_get_mask_account(acc_user_input, masked_acc_num):
    assert get_mask_account(acc_user_input) == masked_acc_num


def test_get_mask_card_number_nonstandard_length():
    with pytest.raises(ValueError):
        get_mask_card_number("7365410843013587430")


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account_nonstandard_length():
    with pytest.raises(ValueError):
        get_mask_account("100123542200127810")


def test_get_mask_account_empty():
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_card_nondigit():
    with pytest.raises(ValueError):
        get_mask_card_number("7 0079 2289 6063")


def test_get_mask_account_nondigit():
    with pytest.raises(ValueError):
        get_mask_account(" 4108 4301 3587 4305")
