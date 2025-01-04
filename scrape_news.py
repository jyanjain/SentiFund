import requests
import json 
from datetime import datetime, timedelta
from newspaper import Article
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokernizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")


stock_name = r'vodafone'

def scrape_newsapi(query = stock_name):
    to_ = datetime.today()
    from_ = to_ - timedelta(days=30)
    country = 'in'

    news_url = f'https://newsapi.org/v2/everything?q={query}&from={from_}&to={to_}&sortBy=popularity&language=en&apiKey={NEWS_API_KEY}'

    response = requests.get(news_url)
    data = response.json()

    articles = data['articles']

    newslist = []
    for article in articles:
        if article['title'] == '[Removed]' or article['description'] == '[Removed]' or article['url'] == '[Removed]' or article['content']  == '[Removed]':
            continue
        filtered = {
            'title' : article['title'],
            'description' : article['description'],
            'url' : article['url'],
            'content' : article['content'],
        }
        newslist.append(filtered)

    with open('news.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(newslist, jsonfile, indent=5)

    return newslist


def news_content(news_item):
    try:
        article = Article(news_item["url"])
        article.download()
        article.parse()
        print("Fetched article")
        return article.text
    except Exception as e:
        print(f"Error fetching article")
        return news_item.get("description", "") 


def analyze_sentiment(news_item):
    content = news_content(news_item)

    text = f"{news_item['title']} {content}"
    
    # Tokenize and get model predictions
    inputs = tokernizer(text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    
    # Convert logits to probabilities
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment_labels = ["negative", "neutral", "positive"]
    
    # Find the sentiment with the highest probability
    sentiment = sentiment_labels[torch.argmax(probs).item()]
    confidence = torch.max(probs).item()
    
    return {"sentiment": sentiment, "confidence": confidence}


news = scrape_newsapi(stock_name)

sentiment_results = []
for new_item in news:
    sentiment = analyze_sentiment(new_item)
    sentiment_results.append({
        "title" : new_item["title"],
        "sentiment": sentiment["sentiment"],
        "confidence": sentiment["confidence"]
    })

# print(sentiment_results)
with open("sentiment_result.json", "w") as file:
    json.dump(sentiment_results, file, indent=4)