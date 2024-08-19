import requests
import os
from dotenv import load_dotenv


load_dotenv()
values = os.getenv("PASSWORD")
keys = os.getenv("API_KEY")
headers = {keys:values}

def currency_conversion(transaction: dict) -> float:
    """Функциz конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers=headers, data=payload)
    result = response.json()
    return result["result"]


if __name__ == '__main__':
    print(currency_conversion({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))