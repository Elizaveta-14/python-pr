import unittest
from src.opertions import count_operations, get_transactions_on_search_bar


class TestBankOperations(unittest.TestCase):
    def test_get_transactions_on_search_bar_basic(self):
        # Пример данных
        data = [
            {"description": "Покупка в магазине"},
            {"description": "Перевод на карту"},
            {"description": "Оплата интернета"}
        ]
        # Пример строки поиска
        search_bar = "интернет"

        # Ожидаемый результат
        expected_result = [
            {"description": "Оплата интернета"}
        ]

        result = get_transactions_on_search_bar(data, search_bar)

        self.assertEqual(result, expected_result)

    def test_get_transactions_on_search_bar_case_insensitive(self):
        # Пример данных
        data = [
            {"description": "Покупка в магазине"},
            {"description": "Перевод на карту"},
            {"description": "Оплата интернета"}
        ]
        # Пример строки поиска
        search_bar = "ИнТеРнЕт"

        # Ожидаемый результат
        expected_result = [
            {"description": "Оплата интернета"}
        ]

        result = get_transactions_on_search_bar(data, search_bar)

        self.assertEqual(result, expected_result)

    def test_count_operations_basic(self):
        # Пример данных
        data = [
            {"description": "Покупка в магазине"},
            {"description": "Перевод на карту"},
            {"description": "Оплата интернета"}
        ]
        # Пример категорий
        categories = ["интернет", "магазин"]

        # Ожидаемый результат
        expected_result = {}

        result = count_operations(data, categories)

        self.assertEqual(result, expected_result)

    def test_count_operations_case_insensitive(self):
        # Пример данных
        data = [
            {"description": "Покупка в магазине"},
            {"description": "Перевод на карту"},
            {"description": "Оплата интернета"}
        ]
        # Пример категорий
        categories = ["ИнТеРнЕт", "МаГаЗиН"]

        # Ожидаемый результат
        expected_result = {}

        result = count_operations(data, categories)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()