import os
import requests
from dotenv import load_dotenv

def make_telegram_message(listing):
    link = listing["link"]
    price = listing["price"]
    room_features = listing["features"]
    #date = f"Datum: {renting_item.get('date', 'onbekend')}"

    message = f"{price} {room_features} \n {link}"

    return message

def send_telegram(listing, CHAT_ID, PRIVATE_KEY):
    url = f"https://api.telegram.org/{PRIVATE_KEY}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": make_telegram_message(listing)
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

def send_telegram_notifications(listing):
    # Load environment variables from .env file
    load_dotenv()
    # Access the API key and private key from environment variables
    CHAT_ID = os.getenv("CHAT_ID")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")

    send_telegram(listing, CHAT_ID, PRIVATE_KEY)


