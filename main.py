import yagmail
import os
from selenium import webdriver
from datetime import datetime
import time
from dotenv import load_dotenv
load_dotenv()


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

# print(type(main()))

def auto_email(cleaned_text):
    subject = "UPDATE: Current Stock Price Percentage"
    message = f"""
    Hello This is to tell you that for your stock it has currently gone down to {cleaned_text} 
    """
    email = yag.send(to=receiver, subject=subject, contents=message)
    return email

def clean_text(percent_text):
    percentage_change = percent_text.strip(" %")
    return float(percentage_change)


def get_price_change():
    driver = get_drivers()
    element = driver.find_element(by="xpath", value="//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]")
    cleaned = clean_text(element.text)
    return cleaned

def decision_maker():
    while True:
        decision_time = datetime.now()
        if decision_time.minute == 30:
            percentage_price_change = get_price_change()
            if percentage_price_change < -0.10:
                auto_email(percentage_price_change)
                print("Email Sent!")
            time.sleep(60)
        time.sleep(10)

decision_maker()









