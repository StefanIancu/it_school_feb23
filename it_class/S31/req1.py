import requests
import time

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
URL2 = "https://jsonplaceholder.typicode.com/comments"


def get_with_retry(url):
    try:
        resp = requests.get(url, timeout=(3.5, 30))     # returneaza obiect request response
    except requests.ConnectTimeout:
        print("Connection timed out.")
        time.sleep(3)
        get_with_retry(url)
    else:
        resp.raise_for_status()
        resp = resp.json()
        for line in resp:
            for k, v in line.items():
                print(k)

try:
    get_with_retry(URL2)
except requests.RequestException as err:
    print(err)


