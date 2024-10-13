import requests

class The_Currency_Converter:
     #Initialise the converter with the API key
    def __init__(self, api_key_1):
        self.api_key_1 = api_key_1
        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key_1}/latest/USD"

    def get_exchange_rate(self, currency_code):
        # get the latest exchange rates from the API
        response = requests.get(self.url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the exchange rate for the specified currency
            return data['conversion_rates'].get(currency_code.upper(), None)
        else:
            print("Error fetching exchange rate")
            return None

    def convert_price(self, price_in_usd, currency_code):
        # Convert a price from USD to the specified currency using the exchange rate
        rate = self.get_exchange_rate(currency_code)
        if rate:
            # Calculate and return the converted price
            return round(price_in_usd * rate, 2)
        else:
            print(f"Currency code {currency_code} not found.")
            return None