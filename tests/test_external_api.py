import unittest
from unittest.mock import patch
import json
import os
import requests
from src.external_api import get_convert_amount, convert_transaction_to_rub
import pytest



@patch("json.loads")
def test_get_convert_amount(mock_get):
    """Проверяет статус коде 200"""
    mock_get.return_value.status_code = 200
    assert get_convert_amount != []


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


@patch("builtins.open", side_effect=KeyError)
def test_file_not_found(amount):
    """Проверяет на возвращение пустого списка при ошибке"""
    transactions = get_convert_amount(amount)
    assert transactions == 0

