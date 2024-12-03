import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def widget():
    """Функция возвращения вывода"""
    return ["Счет ** 4305", "Visa Platinum 700079 ** **** 6361", "Maestro 700079 ** **** 6361",
            "(11.03.2024)"]


def test_mask_account_card():
    """Функция проверки маскировки"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 700079 ** **** 6361"
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 700079 ** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет ** 4305"


def test_get_date():
    """Функция проверки даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "(11.03.2024)"


@pytest.mark.parametrize("numbers_account", ["7000792289606361", "9876543210987654"])
def test_widget_len_account(numbers_account):
    """Функция проверки длинны"""
    assert len(numbers_account) == 16
