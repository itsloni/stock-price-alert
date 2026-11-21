import yagmail
import requests
import os
from selenium import webdriver
import time
from bs4 import BeautifulSoup

sender = os.getenv("gmail_email")
receiver = "rielbumba@gmail.com"
my_password = os.getenv("gmail_password")

print(my_password, sender)

yag = yagmail.SMTP(user=sender, password=my_password)







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

# print(type(main()))

def auto_email():
    percentage_change = main().strip(" %")
    percentage_change = float(percentage_change)
    if percentage_change < -0.10:
        print(percentage_change)
        # if percentage_change > 100:
        subject = "UPDATE: Current Stock Price Percentage"
        message = f"""
        Hello This is to tell you that for your stock it has currently gone down to {percentage_change} 
        """
        yag.send(to=receiver, subject=subject, contents=message)
    else:
        subject = "Current Stock Price Percentage"
        message = f"""
                Hello This is to tell you that for your stock it has currently {percentage_change} 
                """
        yag.send(to=receiver, subject=subject, contents=message)

auto_email()
print("Email Sent!")


