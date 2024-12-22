import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")


def get_convert_amount(currency_code):
    """Проверяет текущий курс валюты"""
    url = "https://www.cbr-xml-daily.ru//daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to get currency rate")
    data = response.json()
    currency_data = data["Valute"].get(currency_code)
    if not currency_data:
        raise ValueError(f"No data for currency {currency_code}")
    return currency_data["Value"]


def convert_transaction_to_rub(transaction):
    """Функция конвертирует сумму транзакции из указанной валюты в рубли"""
    if transaction["currency"] == "USD" or transaction["currency"] == "EUR":
        currency_rate = get_convert_amount(transaction["currency"])
        return float(transaction["amount"]) * currency_rate
    else:
        return float(transaction["amount"])


def process_transaction(transaction):
    """Обрабатывает транзакцию и возвращает словарь"""
    return {
        "currency": transaction["currency"],
        "amount_rub": convert_transaction_to_rub(transaction),
    }
