import pandas as pd
import numpy as np
import json

with open("sentiment_result.json", "r") as file:
    sentiment_data = json.load(file)

with open("fundamentals.json", "r") as file:
    fundamentals = json.load(file)

sentiment_scores = []
for data in sentiment_data:
    sentiment = data['sentiment']
    confidence = data['confidence']

    if sentiment == "positive":
        sentiment_scores.append(confidence)
    elif sentiment == "negative":
        sentiment_scores.append(-confidence)
    else:
        sentiment_scores.append(0)

    
avg_sentiment = np.mean(sentiment_scores)
avg_sentiment_percentage = abs(avg_sentiment) * 100

if avg_sentiment > 0:
    sentiment_trend = "positive"
elif avg_sentiment < 0:
    sentiment_trend = "negative"
else:
    sentiment_trend = "neutral"


stock_name = fundamentals["stock name"]
current_price = fundamentals["current_price"]
volume = fundamentals["volume"]
sales_growth = float(fundamentals["sales_growth"])
croic = fundamentals["croic"]
roce = float(fundamentals["roce"])

# Generate dynamic insights
if sales_growth > 0:
    growth_comment = "The company has shown positive sales growth, indicating potential revenue expansion."
else:
    growth_comment = "The company's sales growth is negative, which might indicate declining revenue trends."

if roce > 0:
    efficiency_comment = "ROCE is positive, indicating efficient capital usage."
else:
    efficiency_comment = "ROCE is negative, highlighting challenges in capital efficiency."

print(f"Media coverage for {stock_name} shows an average sentiment of {sentiment_trend} ({avg_sentiment_percentage:.2f}%).")
print(f"Current Price: {current_price}, Trading Volume: {volume}")
print(f"Sales Growth (YOY): {sales_growth}%, ROCE: {roce}%, CROIC: {croic}%")
print(f"{growth_comment}. {efficiency_comment}")
