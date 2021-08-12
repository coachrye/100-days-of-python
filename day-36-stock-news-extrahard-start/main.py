import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHA_Endpoint = "https://www.alphavantage.co/query"
ALPHA_API_KEY = "K58ZQJP2RE9Q7MHC"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}

response = requests.get(ALPHA_Endpoint, params=parameters)
response.raise_for_status()
stock_data = response.json()
daily_data = stock_data["Time Series (Daily)"]
stock_open = float(daily_data[list(daily_data.keys())[0]]["4. close"])
stock_close = float(daily_data[list(daily_data.keys())[1]]["4. close"])

# TODO: Learn this method
# data_list = [value for (key, value) in daily_data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

stock_difference = abs(stock_open - stock_close)/stock_open
if stock_difference > 0.003:
    # print("Get News")
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_Endpoint = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = "6650e2a4e2384885a5ca47e819b5dec1"

    news_parameters = {
        "q": COMPANY_NAME,
        "sortBy" : "publishedAt",
        "pageSize" : 3,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_Endpoint, params=news_parameters)
    news_response.raise_for_status()
    latest_news = news_response.json()["articles"]

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = "AC7115bff990fa73314af08fc29b00b7ea"  # os.environ['TWILIO_ACCOUNT_SID']
    auth_token = "d91e21ebb42396eed12888ee7a393643"  # os.environ['TWILIO_AUTH_TOKEN']

    if (stock_open - stock_close) > 0:
        stock_difference_message = f"🔺 {round(stock_difference*100,2)}%"
    else:
        stock_difference_message = f"🔻 {round(stock_difference*100,2)}%"

    # TODO: Learn this writing / coding style
    # formatted_articles = [f"Headline: {news['title']} Brief: {news['description']}" for article in latest_news]

    client = Client(account_sid, auth_token)
    for news in latest_news:
        message = client.messages \
            .create(
            body=f"{STOCK}: {stock_difference_message}\n"
              f"Headline: {news['title']}\n"
              f"Brief: {news['description']}",
            from_="+18566175895",
            to="+639062075201"
        )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

