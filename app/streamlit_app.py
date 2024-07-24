# src/app/streamlit_app.py
import streamlit as st

from data.data_fetcher import fetch_stock_data_alpha_vantage, fetch_stock_data_iex
from data.data_processor import process_stock_data_alpha_vantage, process_stock_data_iex
from models.analysis import analyze_trends
from models.recommendation import generate_recommendation

st.title("Smart Financial Advisor")

symbol = st.text_input("Enter Stock Symbol:")
source = st.selectbox("Select Data Source", ["Alpha Vantage", "IEX Cloud"])

if symbol:
    if source == "Alpha Vantage":
        raw_data = fetch_stock_data_alpha_vantage(symbol)
        data = process_stock_data_alpha_vantage(raw_data)
    else:
        raw_data = fetch_stock_data_iex(symbol)
        data = process_stock_data_iex(raw_data)

    st.line_chart(data['close'])

    recommendation = generate_recommendation(data)
    st.write(recommendation)

    trends = analyze_trends(data)
    st.write(trends)
