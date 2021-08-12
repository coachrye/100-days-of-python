from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.ca/LG-34UM69G-B-34-UltraWide-Reduction/dp/B06XFXX5JH"
parameters = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en,en-GB;q=0.9,en-US;q=0.8",
}

response = requests.get(url=URL, headers=parameters)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name="span", id="priceblock_ourprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
