import requests


def currency_conversion(transaction: dict) -> float:
    """Функциz конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    headers = {"apikey": "3unFbSBaLFw7dwlSFoduXLcUmsNnI3xM"}
    response = requests.get(url, headers=headers, data=payload)
    result = response.json()
    return result["result"]
