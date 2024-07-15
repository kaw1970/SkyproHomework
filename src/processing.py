def filter_by_state(list_of_dictionaries: list, key: str = 'EXECUTED') -> list:
    """функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED'), возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_of_dictionaries = [i for i in list_of_dictionaries if i.get('state') == key]
    # new_list_of_dictionaries = []
    # for i in list_of_dictionaries:
    #    if i.get('state') == key:
    #        new_list_of_dictionaries.append(i)
    return new_list_of_dictionaries
