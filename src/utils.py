import requests
import json


def get_transactions(transactions_code):
    """Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей"""
    transactions = []
    url = "https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Couldn't get transaction information")
    return transactions
    with open(transactions_code, "r", encoding="utf-8") as file:
        transaction_content = transactions.read()
        transactions_data = json.loads(transaction_content)
    return transactions
