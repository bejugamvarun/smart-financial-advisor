# src/data/data_storage.py
import os

import pandas as pd


def save_data_to_csv(data, filename):
    data.to_csv(filename)


def load_data_from_csv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename, index_col=0, parse_dates=True)
    return None
