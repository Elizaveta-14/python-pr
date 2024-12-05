transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(transactions: list[dict], currency: str = "USD"):
    """Функция принимает на вход список словарей, и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda transactions_list: transactions_list.get("operationAmount").get("currency").get("code") == currency,
            transactions,
        )
        return filtered_transactions
    else:
        return "Список пустой!"


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(descriptions))


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for i in range(start, stop + 1):
        card_num = str(i).zfill(16)
        yield card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]


for card_number in card_number_generator(1, 5):
    print(card_number)
