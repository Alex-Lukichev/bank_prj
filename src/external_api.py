import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_transaction_amount_rub(transaction: dict, to_currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях."""
    tr_currency = transaction["operationAmount"]["currency"]["code"]
    tr_amount = float(transaction["operationAmount"]["amount"])

    if tr_currency != to_currency:

        load_dotenv(".env")
        API_KEY = os.getenv("APILAYER_API_KEY")
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}"
            f"&from={tr_currency}&amount={tr_amount}"
        )
        payload: Any = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200:
            raise ValueError("Failed to get converted amount")
        data = response.json()
        converted_amount: float = data["result"]
        return round(converted_amount, 2)

    return tr_amount


# from typing import Any, Generator, List
#
# from utils import read_operations

# if __name__ == "__main__":
#
#     def generator_transaction(transactions: List[dict]) -> Generator:
#         for transaction in transactions:
#             yield transaction
#
#     transactions = read_operations("data/operations.json")
#     transaction = generator_transaction(transactions)
#     for _ in range(4):
#         print(get_transaction_amount_rub(next(transaction)))
