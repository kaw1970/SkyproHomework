import masks


def mask_account_card(cart: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах.
    Аргументом может быть строка типа Visa Platinum 7000792289606361
    , или Maestro 7000792289606361, или Счет 73654108430135874305.
    Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!"""
    list_cart_number = cart.split(" ")
    if len(list_cart_number[-1]) == 16:
        list_cart_number[-1] = masks.get_mask_card_number(int(list_cart_number[-1]))
        mask_cart_numer = " ".join(list_cart_number)
        return mask_cart_numer
    else:
        list_cart_number[-1] = masks.get_mask_account(int(list_cart_number[-1]))
        mask_score_numer = " ".join(list_cart_number)
    return mask_score_numer


def get_date(date: str) -> str:
    """
    функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"  и возвращает
    строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    return f'"{date[8:10]}.{date[5:7]}.{date[:4]}"'

