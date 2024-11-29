import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def masks():
    return["700079 ** **** 6361","** 4305"]


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "700079 ** **** 6361"



def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == " ** 4305"
