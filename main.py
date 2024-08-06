import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# URL of the product page
URL = "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"

# Target price
TARGET_PRICE = 1200

# Email credentials
EMAIL_ADDRESS_FROM = os.getenv("EMAIL_ADDRESS_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS_TO = os.getenv("EMAIL_ADDRESS_TO")

# Function to get the price of the product
def get_price():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content,'html.parser')
        # Find the element containing the price
        price_element = (soup.find('div',{'class':'discount_final_price'}).text[2:])
        if price_element:
            price_str = price_element.replace(',','')
            price = float(price_str)
            return price
        else:
            print("Price element not found.")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to send an email
def send_email(price):
    subject = f"🎉 GTA V Price Drop Alert 🚀 Now Only ₹{price}! 🔥 Don't Miss Out! 🎮"
    body = f"""
Hello Palak,

Great news! The price of Grand Theft Auto V has just dropped to an incredible ₹{price}!

This is a fantastic opportunity to get your hands on one of the most popular games at a discounted price. Here are the details:

Game: Grand Theft Auto V
New Price: ₹{price}
Product Page Link: {URL}

Don't wait too long! Such deals don't last forever. Click the link above to secure your copy now.

Happy gaming!

Best regards,
Your Automated Price Monitoring System
"""

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS_FROM
    msg['To'] = EMAIL_ADDRESS_TO
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL_ADDRESS_FROM, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS_FROM, EMAIL_ADDRESS_TO, text)
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to check the price and send an email if the condition is met
def check_price():
    price = get_price()
    if price and price < TARGET_PRICE:
        send_email(price)

# Run the script indefinitely
if __name__ == "__main__":
    while True:
        check_price()
        # Sleep for a day (86400 seconds) before checking again
        time.sleep(86400)