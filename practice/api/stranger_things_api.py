import requests
import time

URL = "https://strangerthings-quotes.vercel.app/api/quotes"

def get_stranger_quote(url):
    try:
        response = requests.get(url, timeout=15)
    except requests.ConnectTimeout:
        print("Connection timed-out! Retrying...")
        time.sleep(3)
        get_stranger_quote(url)
    else:
        response.raise_for_status()
        response = response.json()
        for i in response:
            quote = i["quote"]
            author = i["author"]
            print(f"{quote} - {author}")


while True:

    try:
        time.sleep(3)    
        get_stranger_quote(URL)
    except requests.ConnectTimeout:
        print("Connection error!")

