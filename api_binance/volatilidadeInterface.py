import requests
import json
import math
import tkinter as tk

# ainda precisa corrigir o erro na EMA 9

def calculate_volatility():
    symbol = 'BTCUSDT'
    interval = '1h'

    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=10'
    response = requests.get(url)
    data = json.loads(response.text)

    close_prices = [float(d[4]) for d in data]

    mean = sum(close_prices) / len(close_prices)
    variance = sum([((x - mean) ** 2) for x in close_prices]) / len(close_prices)
    volatility = math.sqrt(variance)

    ema = sum(close_prices[-9:]) / 9

    trend = 'alta' if close_prices[-1] > ema else 'baixa'

    return (volatility, ema, trend)

def analyze():
    volatility, ema, trend = calculate_volatility()
    volatility_label.config(text=f"Volatilidade: {volatility:.2f}")
    ema_label.config(text=f"Média Exponencial de 9 períodos: {ema:.2f}")
    trend_label.config(text=f"Tendência: {trend}")
    
import tkinter as tk

root = tk.Tk()
root.title("Análise de Volatilidade")
root.geometry("400x200")

moeda_label = tk.Label(root, text="Moeda:")
moeda_label.pack()

moeda_entry = tk.Entry(root)
moeda_entry.pack()

tempo_label = tk.Label(root, text="Tempo:")
tempo_label.pack()

tempo_entry = tk.Entry(root)
tempo_entry.pack()

ema_label = tk.Label(root, text="Média Exponencial de 9 períodos:")
ema_label.pack()

ema_entry = tk.Entry(root)
ema_entry.pack()

volatility_label = tk.Label(root, text="")
volatility_label.pack()

trend_label = tk.Label(root, text="")
trend_label.pack()

analyze_button = tk.Button(root, text="Analisar", command=analyze)
analyze_button.pack()

root.mainloop()
