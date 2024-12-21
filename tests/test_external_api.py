from unittest.mock import patch

from src.external_api import convert_transaction_to_rub, get_convert_amount, process_transaction

@patch("requests.get")
def test_get_convert_amount(mock_get):
