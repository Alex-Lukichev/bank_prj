import pytest
from unittest.mock import patch, mock_open
import json
from src.utils import read_operations


# Тест на корректный файл с транзакциями
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file):
    transactions = read_operations("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


# Тест на пустой файл
@patch("builtins.open", new_callable=mock_open, read_data='')
def test_empty_file(mock_file):
    transactions = read_operations("data/operations.json")
    assert transactions == []


# Тест на некорректные данные (например, не список)
@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list(mock_file):
    transactions = read_operations("data/operations.json")
    assert transactions == []



# Тест на случай, если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transactions = read_operations("data/operations.json")
    assert transactions == []





