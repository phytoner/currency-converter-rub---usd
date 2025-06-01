import requests

def get_currency_rate(currency_code):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    return data["Valute"][currency_code]["Value"]

rub = float(input("Сколько рублей перевести?"))
usd_rate = get_currency_rate("USD")
print(f"Это {rub / usd_rate:.2f} долларов.")