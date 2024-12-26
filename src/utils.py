import json


def get_transactions(transactions_code):
    """Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей"""
    transactions = []
    try:

        with open(transactions_code, "r", encoding="utf-8") as file:
            transaction_content = json.load(file)
            return transaction_content
    except FileNotFoundError as ex:
        return transactions
    except json.JSONDecodeError as ex:
        return transactions