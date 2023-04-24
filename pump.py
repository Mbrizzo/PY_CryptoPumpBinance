import requests

symbols = ['BTCUSDT', 'ETHUSDT', 'ARBUSDT']

def get_prices():
    try:
        response = requests.get('https://api.binance.com/api/v3/ticker/price')
        prices = [pair for pair in response.json() if pair['symbol'] in symbols]
        return prices
    except requests.exceptions.RequestException as e:
        print(e)       
 
prices = get_prices()
print(prices) 