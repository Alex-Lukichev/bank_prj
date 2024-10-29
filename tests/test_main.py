from unittest.mock import call

import pytest
from unittest import mock
from main import main
from src.processing import filter_by_state, sort_by_date, json_transactions_reformat, filter_transactions_by_currency
from src.utils import read_operations
from src.read_csv_excel import get_transactions_from_csv, get_transactions_from_excel

from tests.conftest import test_trans

@pytest.fixture
def mock_file_paths():
    """Фикстура для подмены путей к файлам."""
    return {
        'json': 'data/operations.json',
        'csv': 'data/transactions.csv',
        'xlsx': 'data/transactions_excel.xlsx'
    }

@mock.patch("builtins.print")
@mock.patch("builtins.input")
def test_main_function(mock_input, mock_print, test_trans, mock_file_paths):
    """ Тест функции main с симуляцией ввода параметров. """
    mock_input.side_effect = [
        '1',                # Выбор JSON файла
        'EXECUTED',         # Фильтрация по статусу "EXECUTED"
        'да',               # Сортировать по дате
        'по возрастанию',   # Сортировать по возрастанию
        'да',               # Фильтровать только рублевые транзакции
        'да',               # Фильтровать по слову
        'карты',            # Слово для фильтрации
    ]

    with mock.patch("src.utils.read_operations", return_value=test_trans), \
         mock.patch("src.read_csv_excel.get_transactions_from_csv", return_value=test_trans), \
         mock.patch("src.read_csv_excel.get_transactions_from_excel", return_value=test_trans), \
         mock.patch("src.processing.filter_by_state", side_effect=lambda x, y: filter_by_state(x, y)), \
         mock.patch("src.processing.sort_by_date", side_effect=lambda x, y: sort_by_date(x, y)), \
         mock.patch("src.processing.filter_transactions_by_currency", side_effect=lambda x: filter_transactions_by_currency(x)), \
         mock.patch("src.processing.json_transactions_reformat", side_effect=lambda x: json_transactions_reformat(x)):

        main()

        filtered_by_status = [t for t in test_trans if t["state"] == "EXECUTED"]
        assert mock_print.call_count > 0

        sorted_by_date = sort_by_date(filtered_by_status, sort_order=False)
        assert all(sorted_by_date[i]["date"] <= sorted_by_date[i + 1]["date"] for i in range(len(sorted_by_date) - 1))

        ruble_transactions = [t for t in sorted_by_date if t["currency_code"] == "RUB"]
        assert len(ruble_transactions) == len(filter_transactions_by_currency(sorted_by_date))

        filtered_by_word = [t for t in ruble_transactions if "карты" in t["description"].lower()]
        assert len(filtered_by_word) == len([t for t in ruble_transactions if "карты" in t["description"].lower()])

        assert f"Всего банковских операций в выборке: {len(filtered_by_word)}" in str(mock_print.mock_calls)


@mock.patch("builtins.print")
@mock.patch("builtins.input")
def test_main_function_error(mock_input, mock_print, test_trans, mock_file_paths):

    """ Тест функции main с симуляцией ввода параметров. """
    mock_input.side_effect = [
        '4',                # Выбор JSON файла
        'EXECUTED',         # Фильтрация по статусу "EXECUTED"
        'да',               # Сортировать по дате
        'по возрастанию',   # Сортировать по возрастанию
        'да',               # Фильтровать только рублевые транзакции
        'да',               # Фильтровать по слову
        'карты',            # Слово для фильтрации
    ]

    with mock.patch("src.utils.read_operations", return_value=test_trans), \
         mock.patch("src.read_csv_excel.get_transactions_from_csv", return_value=test_trans), \
         mock.patch("src.read_csv_excel.get_transactions_from_excel", return_value=test_trans), \
         mock.patch("src.processing.filter_by_state", side_effect=lambda x, y: filter_by_state(x, y)), \
         mock.patch("src.processing.sort_by_date", side_effect=lambda x, y: sort_by_date(x, y)), \
         mock.patch("src.processing.filter_transactions_by_currency", side_effect=lambda x: filter_transactions_by_currency(x)), \
         mock.patch("src.processing.json_transactions_reformat", side_effect=lambda x: json_transactions_reformat(x)):


        with pytest.raises(ValueError):
            main()
