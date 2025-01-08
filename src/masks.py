import logging
import os


path_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils_log.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename=path_file,
    # filename="../logs/masks_log.log",
    filemode="w",
    )
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    7000 79** **** 6361"""
    card_number_logger.info("Создаю маску номера карты")
    if len(card_number) != 16:
        card_number_logger.error("Неправильный номер карты")
        raise ValueError("Неправильный номер карты")
    card_number_logger.info("Маска номера карты создана")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    **4305"""
    mask_account_logger.info("Создаю маску номера счета")
    if len(account_number) != 20:
        mask_account_logger.error("Неправильный номер счета")
        raise ValueError("Неправильный номер счета")
    mask_account_logger.info("Маска номера счета создана")
    return f" **{account_number[-4:]}"
