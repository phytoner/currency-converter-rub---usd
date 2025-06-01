import requests

def get_exchange_rate(base_currency, target_currency):
    """Получает текущий курс валют с API"""
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        return data['rates'][target_currency]
    except Exception as e:
        print(f"Ошибка при получении курса: {e}")
        return None

def currency_converter():
    """Основная функция конвертера"""
    print("\n💰 Конвертер валют (для выхода введите 'q')")
    
    while True:
        print("\nДоступные валюты: USD, EUR, RUB, CNY, GBP, JPY")
        
        # Ввод данных
        from_curr = input("Из какой валюты: ").upper()
        if from_curr == 'Q':
            break
            
        to_curr = input("В какую валюту: ").upper()
        if to_curr == 'Q':
            break
            
        amount = input("Сумма: ")
        if amount.upper() == 'Q':
            break
            
        try:
            amount = float(amount)
        except ValueError:
            print("Ошибка! Введите числовое значение суммы.")
            continue
            
        # Конвертация
        rate = get_exchange_rate(from_curr, to_curr)
        if rate is None:
            print("Не удалось получить курс. Попробуйте другие валюты.")
            continue
            
        result = amount * rate
        print(f"\nРезультат: {amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        print(f"Курс: 1 {from_curr} = {rate:.4f} {to_curr}")
        
        # Продолжить или выйти
        choice = input("\nПродолжить? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    currency_converter()
    print("\nСпасибо за использование конвертера!")
