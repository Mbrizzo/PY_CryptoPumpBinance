import requests
import time
import pandas as pd
import time

def atualizar_dados(): # pode usar também "crontab -e" (liux)  ou  "Agendador de Tarefas" no windows
    symbol = 'BTCUSDT'

# Define a URL para fazer a solicitação GET
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=24'

# Faz a solicitação GET e armazena a resposta em uma variável
    response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
    # Converte a resposta em uma lista de dicionários
        klines = response.json()    
    current_hour = int(time.time()) // 3600 * 3600 * 1000
    prev_hour = current_hour - 3600 * 1000

# Obtém o volume das últimas 1 hora
    last_1_hour_volume = sum([float(kline[5]) for kline in klines if int(kline[0]) >= current_hour - 3600 * 1000])

# Obtém o volume das 1 hora anteriores
    prev_1_hour_volume = sum([float(kline[5]) for kline in klines if int(kline[0]) >= prev_hour - 3600 * 1000 and int(kline[0]) < current_hour - 3600 * 1000])

# Calcula a variação percentual do volume
    pct_change = (last_1_hour_volume - prev_1_hour_volume) / prev_1_hour_volume * 100 if prev_1_hour_volume > 0 else 0

    print(last_1_hour_volume, prev_1_hour_volume, pct_change)

   # Adiciona os novos dados ao DataFrame
    df = pd.DataFrame({
    'volume de 1h atrás': pd.Series([last_1_hour_volume]),
    'variação': pd.Series([pct_change])
}) 
    
# Grava os dados no arquivo CSV
    df.to_csv('volume.csv', mode='a', index=False, header=False)

while True:
    atualizar_dados()
    time.sleep(3600) 

