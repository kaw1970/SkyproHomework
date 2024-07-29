from typing import Generator, Any


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, str]:
    """Функция выдает транзакции, где валюта операции соответствует заданной."""
    try:
        for i in transactions:
            if i.get("operationAmount").get("currency").get("code") == currency_code:
                yield i
    except StopIteration:
        if transactions == []:
            return "Нет транзакций"
        elif i.get("operationAmount").get("currency").get("code") != currency_code:
            return "Кода валюты нет в транзакциях"


def transaction_descriptions(transactions: list) -> Generator[str, Any, str]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    try:
        for description_operation in transactions:
            yield description_operation.get("description")
    except StopIteration:
        if transactions == []:
            return "Нет транзакций"


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
