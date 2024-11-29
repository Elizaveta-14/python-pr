import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def widget():
    return["Счет ** 4305","Visa Platinum 700079 ** **** 6361","Maestro 700079 ** **** 6361",
           "(11.03.2024)"]


@pytest.mark.parametrize(["info_by_card"],["73654108430135874305"])
def test_mask_account(info_by_card):
    assert len(info_by_card[-16::]) == 16


def test_mask_account_card():
     assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 700079 ** **** 6361"
     assert mask_account_card("Maestro 7000792289606361") == "Maestro 700079 ** **** 6361"
     assert mask_account_card("Счет 73654108430135874305") == "Счет ** 4305"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "(11.03.2024)"
