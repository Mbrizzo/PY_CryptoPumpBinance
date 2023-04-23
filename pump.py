import requests

symbols = ['BTCUSDT', 'ETHUSDT', 'ARBUSDT']

def get_prices():
  
    response = requests.get('https://api.binance.com/api/v3/ticker/price')
    prices = [pair for pair in response.json() if pair['symbol'] in symbols]
    return prices
           
 
prices = get_prices()
print(prices) 