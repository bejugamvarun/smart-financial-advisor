# src/utils/config.py
import os

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY', 'your_alpha_vantage_api_key')
IEX_API_KEY = os.getenv('IEX_API_KEY', 'your_iex_api_key')
NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'your_newsapi_key')
GPT_4_API_KEY = os.getenv('GPT_4_API_KEY', 'your_gpt_4_api_key')
