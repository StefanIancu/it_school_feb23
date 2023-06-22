from apscheduler.schedulers.blocking import BlockingScheduler
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

# sched = BlockingScheduler()

# @sched.scheduled_job('interval', seconds=10)
# def timed_job():
#     print('This job is run every 10 seconds.')

# # @sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
# # def scheduled_job():
# #     print('This job is run every weekday at 10am.')

# # sched.configure(options_from_ini_file)
# sched.start()

