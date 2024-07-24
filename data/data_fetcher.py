# src/data/data_fetcher.py
import requests
from alpha_vantage.timeseries import TimeSeries
from iexfinance.stocks import Stock


def fetch_stock_data_alpha_vantage(symbol):
    ts = TimeSeries(key='your_alpha_vantage_api_key')
    data, _ = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')
    return data


def fetch_stock_data_iex(symbol):
    stock = Stock(symbol, token='your_iex_api_key')
    data = stock.get_quote()
    return data


def fetch_financial_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey=your_newsapi_key'
    response = requests.get(url)
    return response.json()
