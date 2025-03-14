from currency_api import get_exchange_rates

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    if rates:
        if from_currency in rates and to_currency in rates:
            converted_amount = (amount / rates[from_currency]) * rates[to_currency]
            return round(converted_amount, 2)
        else:
            print("Invalid currency code")
            return None
    else:
        print("Failed to fetch exchange rates")
        return None

# Test
if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("Enter source currency (e.g., USD): ").upper()
    to_currency = input("Enter target currency (e.g., EUR): ").upper()
    
    result = convert_currency(amount, from_currency, to_currency)
    if result:
        print(f"{amount} {from_currency} = {result} {to_currency}")

import logging
from currency_api import get_exchange_rates

# Setup logging
logging.basicConfig(filename="conversion.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    if rates:
        if from_currency in rates and to_currency in rates:
            converted_amount = (amount / rates[from_currency]) * rates[to_currency]
            logging.info(f"Converted {amount} {from_currency} to {converted_amount} {to_currency}")
            return round(converted_amount, 2)
        else:
            logging.error("Invalid currency code entered")
            print("Invalid currency code")
            return None
    else:
        logging.error("Failed to fetch exchange rates")
        print("Failed to fetch exchange rates")
        return None
