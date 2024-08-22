import pytest
from src.utils import financial_transactions, transaction_amount


@pytest.fixture
def path():
    return '../data/operations.json'


@pytest.fixture
def path_empty_list():
    return '../data/operations_1.json'


@pytest.fixture
def path_mistake_json():
    return '../data/operations_2.json'


@pytest.fixture
def trans():
    return {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"}
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"}


def test_financial_transactions_nofile():
    assert financial_transactions('nofile') == []


def test_financial_transactions(path):
    assert financial_transactions(path)[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path_empty_list):
    assert financial_transactions(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json):
    assert financial_transactions(path_mistake_json) == []


def test_transaction_amount(trans):
    assert transaction_amount(trans) == '31957.58'
