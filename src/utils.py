import json
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_log_file_path = os.path.join("C:\\Users\\Asus\\PycharmProjects\\pythonProject\\logs\\utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(transactions_code):
    """Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей"""
    transactions = []
    try:
        logger.info("Путь до файла json верный")
        with open(transactions_code, "r", encoding="utf-8") as file:
            transaction_content = json.load(file)
            return transaction_content

    except FileNotFoundError:
        logger.error("Импортируемый список пуст или отсутствует.")
        return transactions
    except json.JSONDecodeError:
        logger.error("Импортируемый список пуст или отсутствует.")
        return transactions


if __name__ == "__main__":
    get_transactions(r"..\data\operations.json")
