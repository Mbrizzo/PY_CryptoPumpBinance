import requests

from dotenv import load_dotenv
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
base_url = 'https://api.binance.com'

def get_pairs():
    endpoint = '/api/v3/exchangeInfo'
    url = base_url + endpoint

    response = requests.get(url)
    response.raise_for_status()

    trading_pairs = []
    for symbol in response.json()['symbols']:
        if symbol['quoteAsset'] == 'USDT':
            trading_pairs.append(symbol['symbol'])

    return trading_pairs

get_pairs = get_pairs()
print(get_pairs)
file = open('pair_usdt.txt', 'w')
for pair in get_pairs:
    file.write(pair + '\n')

file.close()