import requests
import pandas as pd
import time

def atualizar_dados():
# Define o par de criptomoedas para obter as informações
    symbol = 'BTCUSDT'

# Define a URL para fazer a solicitação GET
    url = f'https://api.binance.com/api/v3/trades?symbol={symbol}'

# Define o período de tempo em minutos para calcular a MME
    period = 60

# Faz a solicitação GET e armazena a resposta em uma variável
    response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
    # Converte a resposta em uma lista de dicionários
        trades = response.json()

    # Cria um DataFrame do pandas com os dados dos trades
    df = pd.DataFrame(trades)

    # Converte a coluna 'price' para um tipo numérico
    df['price'] = pd.to_numeric(df['price'])

    # Converte a coluna 'time' para um tipo datetime
    df['time'] = pd.to_datetime(df['time'], unit='ms')

    # Define a coluna 'time' como o índice do DataFrame
    df.set_index('time', inplace=True)
    
    df['price_mme'] = df['price'].ewm(span=period).mean()
    
    df['price_pct_change'] = (df['price'] - df['price_mme']) / df['price_mme'] * 100

    