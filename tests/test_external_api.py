from unittest.mock import patch

import pytest
import requests
from src.external_api import currency_conversion


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


@patch('requests.get')
def test_currency_conversion(mock_get, trans_1):
    mock_get.return_value.json.return_value.return_value["result"] = 1
    assert currency_conversion(trans_1) == 1
