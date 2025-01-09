import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_log_file_path = os.path.join("C:\\Users\\Asus\\PycharmProjects\\pythonProject\\logs\\masks.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    str_number_card = str(number_card)
    if len(str_number_card) == 16:
        logger.info("Формат карты верный")
        return f"{str_number_card[0:6]} {str_number_card[6:4]}** **** {str_number_card[-4:]}"
    else:
        logger.warning("Неверный формат банковской карты")
        return "Не верный формат банковской карты"


def get_mask_account(number_card: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номерапо правилу
    **XXXX"""
    str_number_card = str(number_card)
    logger.info("Успешно")
    return f"{str_number_card[6:4]} ** {str_number_card[-4:]}"
