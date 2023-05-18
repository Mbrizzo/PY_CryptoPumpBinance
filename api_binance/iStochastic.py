import requests

from dotenv import load_dotenv
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
base_url = 'https://api.binance.com'