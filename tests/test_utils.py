from unittest.mock import patch

from src.utils import get_transactions


@patch("json.loads")
def test_get_transactions(mock_get):
    """Проверяет на возвращение списка"""
    mock_get.return_value = []
    assert get_transactions(mock_get) == []
   
