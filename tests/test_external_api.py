# from unittest.mock import patch
#
# from src.external_api import get_convert_amount, process_transaction
#
#
# @patch("json.loads")
# def test_get_convert_amount(mock_get):
#     """Проверяет статус коде 200"""
#     mock_get.return_value.status_code = 200
#     assert get_convert_amount("https://www.cbr-xml-daily.ru//daily_json.js") != "Failed to get currency rate"
#
#
# @patch("json.loads")
# def test_convert_transaction_to_rub(mock_get):
#     """Проверяет на возвращение словаря"""
#     mock_get.return_value.json.return_value = {
#         "date": "2018-02-22",
#         "historical": "",
#         "info": {"rate": 148.972231, "timestamp": 1519328414},
#         "query": {"amount": 1, "from": "USD", "to": "RUB"},
#         "result": 104.461,
#         "success": "true",
#     }

#
# @patch("json.loads")
# def test_convert_amount(mock_get):
#     """Проверяет на валюту"""
#     mock_get.return_value.currency_data = "Valute"
#     assert get_convert_amount("https://www.cbr-xml-daily.ru//daily_json.js") != "No data for currency"
#
#
# @patch("json.loads")
# def test_process_transaction(transaction):
#     assert process_transaction(transaction) != []
#