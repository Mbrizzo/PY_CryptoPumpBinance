import requests
import json
import math
import argparse

parser = argparse.ArgumentParser(description='Calcula a volatilidade, EMA e tendência para um par de moedas.')

parser.add_argument('symbol', type=str, help='o par de moedas a ser analisado')
parser.add_argument('--interval', type=str, default='1h', help='o intervalo de tempo para obter dados de cotação')
parser.add_argument('--limit', type=int, default=10, help='o número de barras de cotação a serem obtidas')
parser.add_argument('--ema', type=int, default=9, help='o número de períodos para calcular a EMA')

args = parser.parse_args()

url = f'https://api.binance.com/api/v3/klines?symbol={args.symbol}&interval={args.interval}&limit={args.limit}'
response = requests.get(url)
data = json.loads(response.text)

close_prices = [float(d[4]) for d in data]

mean = sum(close_prices) / len(close_prices)
variance = sum([((x - mean) ** 2) for x in close_prices]) / len(close_prices)
volatility = math.sqrt(variance)

ema = sum(close_prices[-args.ema:]) / args.ema

trend = 'alta' if close_prices[-1] > ema else 'baixa'

print(f"Volatilidade: {volatility:.2f}")
print(f"Média Exponencial de {args.ema} períodos: {ema:.2f}")
print(f"Tendência: {trend}")

# usage: volatilidade.py [-h] [--interval INTERVAL] [--limit LIMIT] [--ema EMA] 