import sqlite3
from pathlib import Path

from development import BookFlight
from skeleton import FROM as airport

ROOT = Path(__file__).parent
DB_PATH = ROOT / "flights.db"


class Database(BookFlight):
    def __init__(self, path: Path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    @staticmethod
    def read_database():
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        rows = cursor.execute(
            """SELECT "name", "destination", "cost", "ticket" FROM flights
            """
        )
        for row in rows:
            name, destination, cost, ticket = row
            print(f"{name}, {airport}->{destination}, €{cost}, ticket no.{ticket}")
