from typing import Union


def get_mask_card_number(number_card: int) -> str:
    """Функция, принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"


def get_mask_account(number_account: int) -> str:
    """Функция, принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    return f"**{str(number_account)[-4:]}"


number_card = input("Введите номер карты:")
print(get_mask_card_number(int(number_card)))

number_account = input("Введите номер счета:")
print(get_mask_account(int(number_account)))
