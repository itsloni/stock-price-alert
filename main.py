import yagmail
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# def get_stock_price_change_percent():
url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6&tab"
def get_drivers():
    options = webdriver.ChromeOptions()
    options.add_argument("diable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(4)
    return driver


def main():
    driver = get_drivers()
    element = driver.find_element(by="xpath", value="//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]")
    return element.text

print(main())
