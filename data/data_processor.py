# src/data/data_processor.py
import pandas as pd


def process_stock_data_alpha_vantage(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df.index = pd.to_datetime(df.index)
    return df


def process_stock_data_iex(data):
    df = pd.DataFrame([data])
    return df
