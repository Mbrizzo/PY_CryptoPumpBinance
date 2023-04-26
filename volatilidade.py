import requests
import json
import math


response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=10')
data = json.loads(response.text)
close_prices = [float(d[4]) for d in data]

mean = sum(close_prices) / len(close_prices)
variance = sum([((x - mean) ** 2) for x in close_prices]) / len(close_prices)
volatility = math.sqrt(variance)

print(volatility)