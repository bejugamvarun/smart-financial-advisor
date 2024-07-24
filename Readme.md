# Smart Financial Advisor

## Description
Smart Financial Advisor is a real-time web application that provides personalized investment advice, tracks market trends, and generates detailed financial reports using Retrieval-Augmented Generation (RAG) and various financial data APIs.

## Features
- Real-time stock data retrieval from Alpha Vantage and IEX Cloud
- Financial news aggregation
- Personalized investment recommendations
- Financial trend analysis
- Real-time web interface using Streamlit

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-financial-advisor.git
   cd smart-financial-advisor

2. Install dependencies using pipenv
    ```bash
    pipenv install
    ```
   
3. Create a `.env` file in the root directory and add the following environment variables:
   ```bash
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   IEX_API_KEY=your_iex_api_key
   NEWS_API_KEY=your_newsapi_key
   GPT_4_API_KEY=your_gpt_4_api_key
   ```
   
4. Run the Streamlit app:
   ```bash
    pipenv run streamlit run app.py
    ```