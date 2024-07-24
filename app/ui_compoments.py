# src/app/ui_components.py
import streamlit as st


def display_stock_chart(data):
    st.line_chart(data['close'])


def display_recommendation(recommendation):
    st.write(recommendation)
