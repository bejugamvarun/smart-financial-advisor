# src/models/recommendation.py
def generate_recommendation(data):
    latest_close = data['close'].iloc[-1]
    average_close = data['close'].mean()

    if latest_close > average_close:
        return "The stock is performing well. Consider buying."
    else:
        return "The stock is performing below average. You might want to hold off buying."
