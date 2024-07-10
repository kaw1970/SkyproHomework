import masks


def mask_account_card(cart: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах.
    Аргументом может быть строка типа Visa Platinum 7000792289606361
    , или Maestro 7000792289606361, или Счет 73654108430135874305.
    Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!"""
    name_cart = ''
    numer_cart = ''
    list_cart = cart.split()
    for i in list_cart:
        if i.isdigit():
            numer_cart += i
        elif i.isalpha():
            name_cart += i + ' '
    if len(numer_cart) == 16:
        return name_cart + masks.get_mask_card_number(int(numer_cart))
    else:
        mask_score_numer = name_cart + masks.get_mask_account(int(numer_cart))
    return mask_score_numer


def get_date(date: str) -> str:
    """
    функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"  и возвращает
    строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    return f'"{date[8:10]}.{date[5:7]}.{date[:4]}"'
