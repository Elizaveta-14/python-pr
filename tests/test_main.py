import builtins
from typing import Any
from unittest.mock import mock_open, patch

from src.main import choice_state, ending_result, file_selection, filter_by_world, sort_by_rub


transaction_list_sample = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "amount": 31957.58,
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
]

@patch("builtins.input", side_effect="1")
@patch("builtins.open", new_callable=mock_open, read_data="[{amount: 100,currency: USD}]")
@patch("src.utils.get_transaction")
def test_file_selection(mock_get_json: Any, mock_file: Any, mock_input: Any)-> None:
    assert file_selection() == [{"amount: 100,currency: USD"}]