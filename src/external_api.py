import os
from typing import List

from dotenv import load_dotenv
import requests

from src.utils import read_operations


def get_transaction_amount_rub(transaction: dict, to_currency: str = 'RUB') -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях. """
    tr_currency = transaction['operationAmount']['currency']['code']
    tr_amount = transaction['operationAmount']['amount']

    if tr_currency != to_currency:

        load_dotenv('.env')
        API_KEY = os.getenv('API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={tr_currency}&amount={tr_amount}"
        payload = {}
        headers = {
            "apikey": API_KEY
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.status_code)
        # print(response.text)
        if response.status_code != 200:
            raise ValueError(f"Failed to get converted amount")
        data = response.json()
        converted_amount = data.get('result')
        # if not converted_amount:
        #     raise ValueError(f"No data for currency {tr_currency}")
        return round(converted_amount, 2)

    else:
        return tr_amount


"""
Below is a sample response from the endpoint
{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "GBP",
    "to": "JPY"
  },
  "result": 3724.305775,
  "success": true
}
"""

if __name__ == '__main__':

    def generator_transaction(transactions: List[dict]) -> dict:
        for transaction in transactions:
            yield transaction

    transactions = read_operations('data/operations.json')
    transaction = generator_transaction(transactions)
    for _ in range(5):
        print(get_transaction_amount_rub(next(transaction)))

