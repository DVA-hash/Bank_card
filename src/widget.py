from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    number_account_spit = number_account.split()
    if "Счет" in number_account_spit:
        return f"Счет {get_mask_account(number_account_spit[1])}"
    else:
        list_name_card = []
        list_number_card = []
        for i in number_account_spit:
            if i.isalpha():
                list_name_card.append(i)
            if i.isdigit():
                list_number_card.append(i)
        name_card = " ".join(list_name_card)
        number_card = "".join(list_number_card)

        return f"{name_card} {str(get_mask_card_number(number_card))}"


def get_date(date_input: str) -> str:
    """Функция, которая принимает на вход строку и возвращает строку с датой."""
    date_short = date_input[:10].split("-")[::-1]
    date_output = ".".join(date_short)
    return date_output


number_account = input("Введите тип и номер карты или счета:")
print(mask_account_card(number_account))

print(get_date("2024-03-11T02:26:18.671407"))
