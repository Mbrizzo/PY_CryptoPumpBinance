import requests

def get_prices():
    response = requests.get('https://api.binance.com/api/v3/ticker/price')
    return response.json()

prices = get_prices()
print(prices)
