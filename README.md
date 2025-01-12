# Skypro Домашка

## Модуль main.py
Функция main в модуле main отвечает за основную логику проекта и связывает функциональности между собой.
Ожидаемое поведение программы должно быть следующим:
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь: 1

Программа: Для обработки выбран JSON-файл.
Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Пользователь: EXECUTED

Программа: Операции отфильтрованы по статусу "EXECUTED"
В случае, если пользователь ввел неверный статус, программа не должна падать в ошибку, а должна возвращать пользователя 
к вводу корректного статуса:
Пользователь: test

Программа: Статус операции "test" недоступен.

Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю, и 
выводит в консоль операции, соответствующие выборке пользователя:
Программа: Отсортировать операции по дате? Да/Нет

Пользователь: да

Программа: Отсортировать по возрастанию или по убыванию? 

Пользователь: по возрастанию/по убыванию

Программа: Выводить только рублевые тразакции? Да/Нет

Пользователь: да

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD
Если выборка оказалась пустой, программа выводит сообщение:

Программа: Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации

## Модуль masks
1. Принимает номер карты отдает на выход маску номера карты
  - функция get_mask_card_number
  - пример маски номера 7000 79** **** 6361
2. Принимает номер счета отдает на выход маску номера счета
- функция get_mask_account
- пример маски номера **4305

## Модуль widget 
1. Принимает имя и номер карты или счета отдает на выход имя и маску номера карты или счета
- функция mask_account_card
- привер ввода: Visa Platinum 7000 7922 8960 6361
- Счет 73654108430135874305
- Visa Classic 6831982476737658
2. Маску номера получает в модуле masks

## Модуль processing
1. Принимает список словарей и возвращает отсортированный по ключу "state"
2. функция filter_by_state
3. Принимает список словарей и возвращает отсортированный по ключу "date"
- функция sort_by_date
- сортировка True - по убыванию, False - по возрастанию

## Модуль generators
1. Функция filter_by_currency выдает транзакции, где валюта операции соответствует заданной.
2. Функция transaction_descriptions принимает список словарей с транзакциями и возвращает описание 
   каждой операции по очереди.
3. Функция card_number_generator может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
 
## Модуль utils
1. Функция financial_transactions принимает на вход путь до JSON-файла и возвращает список словарей с данными о 
финансовых транзакциях.
2. JSON-файл находится в директории data.
3. Функция transaction_amount принимает на вход транзакцию и возвращает сумму транзакции в рублях.

## Модуль external_api
1. Функция конвертации currency_conversion, используется функцией transaction_amount, если валюта транзакции не рубль.

## Модуль transactions_csv_excel
1. Функция transactions_csv для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента, 
выдает список словарей с транзакциями..
2. Функция transactions_excel для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве 
аргумента, выдает список словарей с транзакциями.

## Модуль banking_operations_filter.py
1. Функция filter_banking_transactions_by_description принимает список словарей с данными о банковских операциях и 
строку поиска, а возвращает список словарей, у которых в описании есть данная строка.
2. Функция filter_banking_description принимает список словарей с данными о банковских операциях и список категорий 
операций, а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в 
каждой категории. Категории операций хранятся в поле description.

#### Docstring и аннотации типов
1. все функции должны содержать docstring и корректные аннотации типов. 
2. Пример docstring:
    ```python
   def example_function(param1: int, param2: str) -> bool:
         """
         Описание функции.
         :param param1: Описание параметра 1
         :param param2: Описание параметра 2
         :return: Описание возвращаемого значения
         """
         pass
     ```
   
##### Инструкции по установке проекта
1. Клонируйте репозиторий:
          ```bash
          git clone https://github.com/kaw1970/SkyproHomework.git
          ```
       2. Перейдите в директорию проекта:
          ```bash
          cd SkyproHomework
          ```
       3. Установите зависимости:
          ```bash
          pip install -r requirements.txt
          ```
2. Необходимые зависимости
    - Python 3.8+
    - Другие зависимости указаны в файле `requirements.txt`
3. Конфигурация
    - Создайте файл `.env` и добавьте необходимые переменные окружения.
    - Пример конфигурации:
          ```env
          VARIABLE_NAME=value
          ```

###### Тестирование
1. Тесты расположены в папке test
2. Охват тестирования 100%
3. Для проверки функций filter_by_currency и transaction_descriptions модуль generators:
4. """transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)"""

###### Логирование
1. Файлы логов записываются в папку logs
2. Для модуля masks.py - masks_log.log
3. Для модуля utils.py - utils_log.log
4. Файлы логов перезаписываемые
