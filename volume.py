import requests

# Define o par de criptomoedas para obter as informações
symbol = 'BTCUSDT'

# Define a URL para fazer a solicitação GET
url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=24'

# Faz a solicitação GET e armazena a resposta em uma variável
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta em uma lista de dicionários
    klines = response.json()
    print(response)