import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_convert_amount(currency_code, amount):
    """Проверяет текущий курс валюты"""
    try:
        if currency_code == "USD" or currency_code == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                json_result = response.json()
                rub_amount = json_result["result"]
                return round(rub_amount, 2)
            else:
                return 0
        else:
            return 0
    except KeyError:
        return 0

def convert_transaction_to_rub(transaction):
    """Функция конвертирует сумму транзакции из указанной валюты в рубли"""
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        currency_rate = get_convert_amount(currency_code, amount)
        return currency_rate
    else:
        return float(transaction["operationAmount"]["amount"])


def process_transaction(transaction):
    """Обрабатывает транзакцию и возвращает словарь"""
    return {
        "currency": transaction["currency"],
        "amount_rub": convert_transaction_to_rub(transaction),
    }
