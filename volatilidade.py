import requests
import json
import math


response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=10')
data = json.loads(response.text)
close_prices = [float(d[4]) for d in data]

print(close_prices)