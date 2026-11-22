# Stock Price Alert

A Python script that monitors the CROBEX stock index percentage change from the Zagreb Stock Exchange website and sends an email alert when the percentage drops below **-0.1%**.

## Features

- Scrapes live stock percentage change using Selenium + BeautifulSoup
- Sends email notification when the drop is significant
- Handles JavaScript-rendered content
- Simple and easy to run

## Technologies Used

- Python
- Selenium
- yagmail (or smtplib)
- python-dotenv (for environment variables)

## Project Structure

```text
stock-price-alert/
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itsloni/stock-price-alert.git
cd stock-price-alert
```
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the project root and add your email credentials:

```text
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

2. Make sure you have Chrome installed (Selenium will use it).

## How to Run

```bash
python main.py
```

## Notes

- The target website loads data with JavaScript, so Selenium is required.
- The script checks the percentage change and sends an email only if it goes below -0.1%.
- You can schedule this script to run periodically using Task Scheduler (Windows) or cron (Linux/Mac).

## Author

Ayoola Oluwalonimi Emmanuel (itsloni)
