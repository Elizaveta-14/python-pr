from unittest.mock import patch


from src.utils import get_transactions


@patch("json.loads")
def test_get_transactions(mock_get):
    """Проверяет на возвращение списка"""
    mock_get.return_value = ""
    assert get_transactions(mock_get) == ""


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_no_found(mock_file):
    """Проверяет на возвращение пустого списка при ошибке"""
    transactions = get_transactions("data/operations.json")
    assert transactions == []
