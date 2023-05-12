import requests

def get_prices():
    response = requests.get('https://api.binance.com/api/v3/ticker/price')
    return response.json()

#prices = get_prices()

def crossover(symbol, start_time):
    url = 'https://api.binance.com/api/v3/klines'
    interval = "1m"
    params = { 'symbol' : symbol,
                'interval' : interval,
                'startTime': start_time
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        klines = response.json()
        return klines
    else:
        print("Error:", response.status_code)
        return None

cross= crossover('BTCUSDT', 1620753780000)
print(cross)