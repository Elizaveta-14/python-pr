import unittest
from unittest.mock import patch

from src.external_api import convert_transaction_to_rub, get_convert_amount


@patch("json.loads")
def test_get_convert_amount(mock_get):
    """Проверяет статус коде 200"""
    mock_get.return_value.status_code = 200
    assert get_convert_amount != 0


@patch("json.loads")
def test_convert_transaction_to_rub(mock_get):
    """Проверяет на возвращение словаря"""
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 1, "from": "USD", "to": "RUB"},
        "result": 104.461,
        "success": "true",
    }


class TestConvertTransactionToRub(unittest.TestCase):
    @patch("src.external_api.get_convert_amount")
    def test_convert_transaction_to_rub_usd(self, mock_get_convert_amount):
        """Проверяем результат в USD"""

        transaction = {
            "id": 1,
            "state": "COMPLETED",
            "date": "2021-01-01T00:00:00",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "доллар", "code": "USD"}},
        }

        mock_get_convert_amount.return_value = 75000.00
        result = convert_transaction_to_rub(transaction)
        expected_result = 75000.00
        self.assertEqual(result, expected_result)

    @patch("src.external_api.get_convert_amount")
    def test_convert_transaction_other_currency(self, mock_get_convert_amount):
        """Проверяет не отсутствие ключа"""

        transaction = {
            "id": 3,
            "state": "COMPLETED",
            "date": "2021-01-03T00:00:00",
            "operationAmount": {"amount": "3000.00", "currency": {"name": "другая валюта", "": ""}},
        }

        mock_get_convert_amount.return_value = None
        with self.assertRaises(KeyError):
            convert_transaction_to_rub(transaction)

    @patch("src.external_api.get_convert_amount")
    def test_convert_transaction_to_rub_eur(self, mock_get_convert_amount):
        """Проверяет результата EUR"""

        transaction = {
            "id": 2,
            "state": "COMPLETED",
            "date": "2021-01-02T00:00:00",
            "operationAmount": {"amount": "2000.00", "currency": {"name": "евро", "code": "EUR"}},
        }

        mock_get_convert_amount.return_value = 170000.00
        result = convert_transaction_to_rub(transaction)
        expected_result = 170000.00
        self.assertEqual(result, expected_result)
