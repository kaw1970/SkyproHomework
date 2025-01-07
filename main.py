# coding: utf-8
import os

from src.processing import filter_by_state
from src.transactions_csv_excel import transactions_csv, transactions_excel
from src.utils import financial_transactions



def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    menu = int(input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    : """))
    if menu == 1:
        print("Для обработки выбран JSON-файл.")
        path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        trans = financial_transactions(path_to_file)
        print(trans)
    elif menu == 2:
        print("Для обработки выбран CSV-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
        trans = transactions_csv(path)
        print(trans)
    else:
        print("Для обработки выбран XLSX-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
        trans = transactions_excel(path)

    state = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: 
            EXECUTED, CANCELED, PENDING
            :""")
    state = state.upper()
    while state != 'EXECUTED' and state != 'CANCELED' and state != 'PENDING':
        print(f'Статус операции "{state}" недоступен.')
        state = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
                    Доступные для фильтровки статусы: 
                    EXECUTED, CANCELED, PENDING
                    :""")
        state = state.upper()
    else:
        if state == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
        elif state == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
        else:
            print('Операции отфильтрованы по статусу "PENDING"')

    filter_trans = filter_by_state(trans, state)
    print(filter_trans)


if __name__ == '__main__':
    main()
