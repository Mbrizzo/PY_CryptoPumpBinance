import requests
import numpy as np

def get_close_prices(trading_pair):
    url = f"https://api.binance.com/api/v3/klines?symbol={trading_pair}&interval=1m&limit=14"
    response = requests.get(url)
    
    response.status_code == 200
    kline_data = response.json()      
    close_prices = np.array([float(data[4]) for data in kline_data])

    return close_prices

prices = get_close_prices('BTCUSDT')
print(prices)