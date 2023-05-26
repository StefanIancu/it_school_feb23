import sqlite3
from pathlib import Path
from ticket import PlaneTicket
from cli_menu import BookFlight

ROOT = Path(__file__).parent
DB_PATH = ROOT / "flights.db"


# connection = sqlite3.connect(DB_PATH)
# cursor = connection.cursor()

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
            print(row)
        


