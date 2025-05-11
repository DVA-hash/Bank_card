from typing import Dict, List


def filter_by_state(list_dictionaries: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция, принимает на вход список словарей и опционально значение для ключа
    и возвращает новый список словарей, содержащий только те словари, у которых
    ключ соответствует указанному значению.
    """
    return ([dictionary for dictionary in list_dictionaries if dictionary.get('state') == state])


def sort_by_date(list_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, принимает список словарей и необязательный параметр,
    задающий порядок сортировки  и возвращает новый список, отсортированный по дате
    """
    return sorted(list_dictionaries, key=lambda x: x.get("date"), reverse=reverse)


list_dictionaries = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
