import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def masks():
    """Функция возвращения вывода"""
    return["700079 ** **** 6361","** 4305"]


def test_get_mask_card_number():
    """Функция проверки маскировки карты по принципу XXXX XX** **** XXXX"""
    assert get_mask_card_number(7000792289606361) == "700079 ** **** 6361"



def test_get_mask_account():
    """Функция проверки маскировки карты по принципу **XXXX"""
    assert get_mask_account(73654108430135874305) == " ** 4305"


@pytest.mark.parametrize("number_account", ["7000792289606361", "73654108430135874305"])
def test_masks_len_account(number_account):
    """Функция проверки длинны"""
    assert len(number_account) > 0