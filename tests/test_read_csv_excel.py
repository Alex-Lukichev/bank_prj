from pathlib import Path
from unittest.mock import patch

from src.read_csv_excel import get_transactions_from_csv, get_transactions_from_excel

BASE_DIR = Path(__file__).resolve().parent.parent
file_path_csv = BASE_DIR / "data" / "transactions.csv"
file_path_excel = BASE_DIR / "data" / "transactions_excel.xlsx"


@patch("src.read_csv_excel.pd.read_csv")
def test_get_transactions_from_csv(mock_read, test_df):
    """Тестирование функции чтения csv файла. Mock возвращает тестовый DataFrame из фикстуры test_df."""
    mock_read.return_value = test_df
    result = get_transactions_from_csv(file_path_csv)
    expected = test_df.to_dict(orient="records")
    assert result == expected


def test_get_transactions_from_csv_incorrect_path():
    """Тестирование функции чтения csv файла. Некорректный путь к файлу."""
    assert get_transactions_from_csv("") == []


@patch("src.read_csv_excel.pd.read_excel")
def test_get_transactions_from_excel(mock_read, test_df):
    """Тестирование функции чтения Excel файла. Mock возвращает тестовый DataFrame из фикстуры test_df."""
    mock_read.return_value = test_df
    result = get_transactions_from_excel(file_path_excel)
    expected = test_df.to_dict(orient="records")
    assert result == expected


def test_get_transactions_from_excel_incorrect_path():
    """Тестирование функции чтения Excel файла. Некорректный путь к файлу."""
    assert get_transactions_from_excel("") == []
