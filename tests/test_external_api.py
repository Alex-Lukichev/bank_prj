import pytest
import unittest
from unittest.mock import patch, MagicMock
from src.external_api import get_transaction_amount_rub

class TestGetTransactionAmountRub(unittest.TestCase):

    @patch('os.getenv')
    @patch('requests.request')
    def test_conversion_to_rub(self, mock_request, mock_getenv):
        mock_getenv.return_value = 'mock_api_key'
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": 772000.00
        }
        mock_request.return_value = mock_response
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
        amount_rub = get_transaction_amount_rub(transaction)
        assert amount_rub == 772000.00
        mock_getenv.assert_called_once_with('API_KEY')
        mock_request.assert_called_once()


    @patch('os.getenv')
    @patch('requests.request')
    def test_failed_api_call(self, mock_request, mock_getenv):
        mock_getenv.return_value = 'mock_api_key'
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
        with self.assertRaises(ValueError):
            get_transaction_amount_rub(transaction)
        mock_getenv.assert_called_once_with('API_KEY')
        mock_request.assert_called_once()
