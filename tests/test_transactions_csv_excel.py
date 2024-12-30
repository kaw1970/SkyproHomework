from unittest.mock import patch

import pytest


from src.transactions_csv_excel import transactions_excel, transactions_csv


@patch('pandas.read_csv')
def test_transactions_csv(mock):
    mock.return_value.to_dict.return_value = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                               'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                               'from': 'Счет 58803664561298323391',
                                               'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                                              {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
                                               'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP',
                                               'from': 'Discover 3172601889670065',
                                               'to': 'Discover 0720428384694643',
                                               'description': 'Перевод с карты на карту'}]
