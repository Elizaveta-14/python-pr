from main import get_mask_card_number, get_mask_account


def mask_account_card(card: str) -> str:
    """Функция выделяет цифры и буквы из строки."""
    if "Счет" in card:
        return get_mask_account(card)
    else:
        cards = get_mask_card_number(card[-16:])
        new_card = card.replace(card[-16:], cards)
        return new_card


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))


def get_date(date: str) -> str

