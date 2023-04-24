import requests
import time
import pandas as pd

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

# Obtém o volume das últimas 2 horas
    current_hour = int(time.time()) // 3600 * 3600 * 1000
    prev_hour = current_hour - 3600 * 1000
    last_2_hours_volume = sum([float(kline[5]) for kline in klines if int(kline[0]) >= prev_hour])
    print(last_2_hours_volume)

# Obtém o volume das 2 horas anteriores
    prev_2_hours_volume = sum([float(kline[5]) for kline in klines if int(kline[0]) >= prev_hour - 3600 * 1000])

    # Calcula a variação percentual do volume
    pct_change = (last_2_hours_volume - prev_2_hours_volume) / prev_2_hours_volume * 100 if prev_2_hours_volume > 0 else 0
    with open("v2.txt", "w") as f:    
        f.write(f" Volume das últimas 2 horas{last_2_hours_volume}\n")
        f.write(f" Variação percentual{pct_change}")

   # Adiciona os novos dados ao DataFrame
    df = pd.DataFrame({
    'volume de 2h atrás': pd.Series([last_2_hours_volume]),
    'variação': pd.Series([pct_change])
})
    # Imprime as informações
    print(f'Par de criptomoedas: {symbol}')
    print(f'Variação percentual no volume nas últimas 2 horas: {pct_change:.2f}%')
    print(f'Volume das últimas 2 horas: {last_2_hours_volume:.2f}')
else:
    print(f'Erro: {response.status_code}/n')

# Grava os dados no arquivo CSV
df.to_csv('volume.csv', mode='a', index=False, header=False)