import requests
import time

URL = "https://api.oceandrivers.com:443/v1.0/getWeatherDisplay/bucharest/?period=latestdata"


def get_weather(url):
    try:
        response = requests.get(url)
    except requests.ConnectTimeout:
        print("Connection timed out - retrying...")
        time.sleep(3)
        get_weather(url)
    else:
        response.raise_for_status()
        resp = response.json()
        for k, v in resp.items():
            print(k, v)



get_weather(URL)