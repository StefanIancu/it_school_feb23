import random
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent

DESTINATIONS_AND_PRICES = {
    "timisoara": 150,
    "budapest": 150,
    "bratislava": 165,
    "sofia": 150,
    "prague": 200,
    "berlin": 250,
    "rome": 400,
    "paris": 350,
    "basel": 550,
    "tokyo": 999,
}


now = date.today()
FROM = "Bucharest OTP"
DATE = f"{now.month}.{now.year}"

GATE = random.choice(range(30))
