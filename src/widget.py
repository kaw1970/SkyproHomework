import masks


def mask_account_card(cart: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах.
    Аргументом может быть строка типа Visa Platinum 7000792289606361
    , или Maestro 7000792289606361, или Счет 73654108430135874305.
    Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!"""
    list_cart_number = cart.split(' ')
    if len(list_cart_number[-1]) == 16:
        list_cart_number[-1] = masks.get_mask_card_number(int(list_cart_number[-1]))
        mask_cart_numer = ' '.join(list_cart_number)
        return mask_cart_numer
    else:
        list_cart_number[-1] = masks.get_mask_account(int(list_cart_number[-1]))
        mask_score_numer = ' '.join(list_cart_number)
    return mask_score_numer


if __name__ == "__main__":
    test = ['Maestro 1596837868705199', 'Счет  64686473678894779589', 'MasterCard 7158300734726758',
            'Счет 35383033474447895560', 'Visa Classic 6831982476737658', 'Visa Platinum 8990922113665229',
            'Visa Gold 5999414228426353', 'Счет 73654108430135874305']
    for i in test:
        over = mask_account_card(i)
        print(over)
