import pytest

from src.search_func import get_search_transactions, get_transactions_count

def test_get_search_transactions_match(test_trans):
    search_str = "Перевод с карты на карту"
    result = get_search_transactions(test_trans, search_str)
    assert len(result) == 3
    assert all(search_str in tr['description'] for tr in result)

def test_get_search_transactions_no_match(test_trans):
    search_str = "Nonexistent description"
    result = get_search_transactions(test_trans, search_str)
    assert result == []

def test_get_transactions_count(test_trans):
    categories = ["Перевод с карты на карту", "Открытие вклада", "Перевод организации"]
    result = get_transactions_count(test_trans, categories)
    assert result == {
        "Перевод с карты на карту": 3,
        "Открытие вклада": 2,
        "Перевод организации": 2
    }

def test_get_transactions_count_empty_category(test_trans):
    categories = ["Тест несуществующее описание"]
    result = get_transactions_count(test_trans, categories)
    assert result == {}