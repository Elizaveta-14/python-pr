from unittest.mock import patch

from src.utils import get_transactions


@patch("json.loads")
def test_get_transactions(mock_get):
    """Проверяет на возвращение списка"""
    mock_get.return_value = []
    assert get_transactions("https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view") == []
