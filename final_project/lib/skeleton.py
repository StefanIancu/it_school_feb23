from pathlib import Path
import random

ROOT = Path(__file__).parent

DESTINATIONS_AND_PRICES = {
                "bucharest": 150, "budapest": 150, "bratislava": 165, 
                "sofia": 150, "prague": 200, "berlin": 250, "rome": 400,
                "paris": 350, "basel": 550, "tokyo": 999 
                }

FLIGHTS = []

FROM = "Bucharest OTP"
MONTH = "06.2023"

GATE = random.choice(range(30))

