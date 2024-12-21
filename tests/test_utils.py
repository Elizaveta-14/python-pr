from unittest.mock import patch

import requests

from src.utils import get_transactions


@patch('requests.get')
def test_get_transactions(mock_get):
    mock_get.return_value.json.return_value = {"test_dict": "01", "test_key": "test_values_1"}

    mock_get.assert_called_once_with('https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view')


