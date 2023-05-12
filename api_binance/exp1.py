import requests
import pandas as pd
import numpy as np
import time

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
    data = response.json()
    
    columns = ['open_time',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'close_time',
            'quote_asset_volume',
            'trades',
            'taker_buy_base_asset_volume',
            'taker_buy_quote_asset_volume',
            'ignore'
            ]
    # cria um objeto DataFrame do pandas a partir dos dados recebidos na resposta da API Binance
    data_df = pd.DataFrame(data, columns=columns)
    # converte todos os valores do DataFrame para o tipo float
    data_df = data_df.astype(float)
    # converte a coluna 'open_time' do DataFrame de um valor numérico em milissegundos para um objeto datetime
    data_df['open_time'] = pd.to_datetime(data_df['open_time'], unit='ms')
    # define a coluna 'open_time' como índice do DataFrame
    data_df.set_index('open_time', inplace=True)    

#cross= crossover('BTCUSDT', 1620753780000)
#print(cross)
#file = open('resultados.txt', 'w')
#file.write(str(cross))
#file.close()
