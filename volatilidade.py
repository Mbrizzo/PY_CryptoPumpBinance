import requests
import json
import math


symbol = 'BTCUSDT'
interval = '1h'

url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=10'
response = requests.get(url)
data = json.loads(response.text)

# Debugging
print(data) # imprime a lista de candlesticks
print(len(data)) # imprime o tamanho da lista de candlesticks

close_prices = [float(d[4]) for d in data]

mean = sum(close_prices) / len(close_prices)
variance = sum([((x - mean) ** 2) for x in close_prices]) / len(close_prices)
volatility = math.sqrt(variance)

ema = sum(close_prices[-9:]) / 9

trend = 'alta' if close_prices[-1] > ema else 'baixa'

print(f"Volatilidade: {volatility:.2f}")
print(f"Média Exponencial de 9 períodos: {ema:.2f}")
print(f"Tendência: {trend}")