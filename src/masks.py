def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    str_number_card = str(number_card)
    return f"{str_number_card[0:6]} {str_number_card[6:4]}** **** {str_number_card[-4:]}"


def get_mask_account(number_card: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номерапо правилу
    **XXXX"""
    str_number_card = str(number_card)
    return f"{str_number_card[6:4]} ** {str_number_card[-4:]}"
