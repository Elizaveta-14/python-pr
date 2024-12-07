import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def generators():
    return [
        {
            "id": 970157810,
            "date": "2018-06-08T10:3:58.027767",
            "operationAmount": {"amount": "150", "currency": {"code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        }
    ]


@pytest.mark.parametrize("currency", ["result"])
def test_filter_by_currency(generators, currency) -> None:
    """Функция проверяет что список не пустой"""
    generator = filter_by_currency(generators)
    assert next(generator) != []


@pytest.mark.parametrize("description", ["Перевод организации"])
def test_transaction_descriptions(generators, description):
    """Функция проверяет генератор на результат"""
    generator = transaction_descriptions(generators)
    assert next(generator) == description


@pytest.fixture
def generator():
    return [{"0000 0000 0000 0001"}, {"0000 0000 0000 0002"}]


@pytest.mark.parametrize("number_generator", ["0000 0000 0000 0001"])
def test_card_number_generator(generator, number_generator):
    """Функция проверки длинны"""
    assert len(number_generator) > 0
