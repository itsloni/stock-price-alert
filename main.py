import yagmail
import requests
from bs4 import BeautifulSoup

# def get_stock_price_change_percent():
url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
content = requests.get(url)
soup = BeautifulSoup(content.text, "html.parser")
rate = soup.find_all("span", {"class": "rate"})
print(soup)
