import re


def filter_banking_transactions_by_description(banking_description: list, search_bar: str) -> list:
    """������� ��������� ������ �������� � ������� � ���������� ��������� � ������ ������, � ���������� ������ ��������,
    � ������� � �������� ���� ������ ������."""
    pattern = search_bar
    string_ = []
    for description in banking_description:
        dict_string = str(description)
        if re.search(pattern, dict_string, flags=re.IGNORECASE):
            string_.append(dict_string)
    return string_


def filter_banking_description(banking_description: list, categories_operations: list) -> dict:
    """������� ��������� ������ �������� � ������� � ���������� ��������� � ������ ��������� ��������, � ���������� 
    �������, � ������� ����� � ��� �������� ���������, � �������� � ��� ���������� �������� � ������ ���������. 
    ��������� �������� �������� � ���� description."""
    result = {}
    for categories in categories_operations:
        pattern = categories
        description = str(banking_description)
        string_ = re.findall(pattern, description, flags=re.IGNORECASE)
        values = len(string_)
        result[categories] = values
    return result
