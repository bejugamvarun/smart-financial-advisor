# src/models/analysis.py
def analyze_trends(data):
    data['price_change'] = data['close'].pct_change()
    return data
