import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "YOUR STOCK API"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "YOUR NEWS API KEY"

ACCOUNT_SID = "YOUR ACCOUNT SID"
AUTH_TOKEN = "YOUR AUTH TOKEN"

# GETTING THE DATES
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
one_day_ago = now - timedelta(days=1)
two_day_ago = now - timedelta(days=2)
formatted_one_day_ago = one_day_ago.strftime("%Y-%m-%d") + " " + "19:00:00"
formatted_two_day_ago = two_day_ago.strftime("%Y-%m-%d") + " " + "19:00:00"
print(formatted_one_day_ago)
print(formatted_two_day_ago)
dates = [formatted_one_day_ago, formatted_two_day_ago]


# PARAMETERS FOR API
stocks_parameters = {
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_INTRADAY",
    "interval": "60min",
    "apikey": STOCK_API,
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
}

# STOCK API FUNCTIONING
stock_endpoint = requests.get(STOCK_ENDPOINT, params=stocks_parameters)
data = stock_endpoint.json()
stock_endpoint.raise_for_status()
stock = [data["Time Series (60min)"][i]["4. close"] for i in dates]
print(data["Time Series (60min)"][formatted_one_day_ago]["4. close"])
print(data["Time Series (60min)"][formatted_two_day_ago]["4. close"])


# Calculating percentage
difference = float(stock[0]) - float(stock[1])
percentage_difference = round((difference / float(stock[0])) * 100)
print(percentage_difference)

emoji = None
if percentage_difference > 0:
    emoji = "📈"
else:
    emoji = "📉"

# Fetching news if the stock increases or decreases by 5 percent.
if percentage_difference < 5 or percentage_difference > -5:
    # NEWS API FUNCTIONING
    news_endpoint = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_endpoint.json()["articles"][:3]

    # FORMATTING ARTICLES
    formatted_article = [f"{STOCK_NAME}: {emoji}{abs(percentage_difference)}%\nHeadlines: {data['title']}.\nBrief: {data['description']}" for data in articles]

    # SENDING SMS VIA TWILIO
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for news in formatted_article:
        message = client.messages \
            .create(
            body=f"{news}",
            from_="+15109014405",
            to="YOUR PHONE NUMBER"
        )
        print(message.status)
