import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

path_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils_log.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename=path_file,
    # filename="../logs/utils_log.log",
    filemode="w",
    )
financial_transactions_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        financial_transactions_logger.info("Открываю файл с транзакциями")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                financial_transactions_logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            financial_transactions_logger.error("Список транзакций пуст")
            return []
        financial_transactions_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        financial_transactions_logger.error("Файл с транзакциями не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        transaction_amount_logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(trans)
        transaction_amount_logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount
