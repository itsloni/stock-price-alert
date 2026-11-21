import yagmail
import requests
from bs4 import BeautifulSoup

# def get_stock_price_change_percent():
url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6&tab"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
change_percentage = soup.find_all("span", class_="stock-value")
print(change_percentage)
