import sqlite3
from pathlib import Path

from development import BookFlight
from development import WhereToGo
from skeleton import FROM as airport
from skeleton import DESTINATIONS_AND_PRICES

ROOT = Path(__file__).parent
DB_PATH = ROOT / "flights.db"



class Database(BookFlight):
    def __init__(self, path: Path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    @staticmethod
    def read_database():
        """Method that shows the booked flights."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        rows = cursor.execute(
            """SELECT "name", "destination", "cost", "ticket" FROM flights
            """
        )
        for row in rows:
            name, destination, cost, ticket = row
            print(f"{name}, {airport}->{destination}, €{cost}, ticket no.{ticket}")


    @staticmethod
    def add_flight():
        """Method that adds a flight to the "flights" database containing 
        destination, flight number, departure time and number of seats left."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        destination = input("Destination: ")
        flight_number = input("Flight number: ")
        time = input("Departure time: ")
        seats = input("Number of seats: ")
        cursor.execute(
            """INSERT INTO departures ("destination", "flight_number", "time", "seats ") VALUES (?, ?, ?, ?)""",
            (destination.title(), flight_number, time, seats)
        )
        connection.commit()


    @staticmethod
    def read_flights():
        """Method that reads from a database of flights a specific destination
        which the user chooses."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        while True:
            destination = input("What destination interests you? ")
            if destination.lower() in DESTINATIONS_AND_PRICES.keys():
                rows = cursor.execute(
                """SELECT * FROM departures WHERE "destination" is ?""",
                    (destination.title(), )
                )
                break
            else:
                print("We currently don't fly there. Please see our list of destinations.")
                WhereToGo.see_list_of_destinations()


        print(f"Upcoming flights for {destination.title()}:")
        for row in rows:
            dest, flight_nr, dep_time, seats = row
            print(f"{airport}-> {dest}, flight number {flight_nr}, departure at {dep_time}, available seats {seats}.")


    @staticmethod
    def get_ticket_existence():
        """Method that returns bool if a specific ticket is in flights database
        in order to help the delete_reservation method to be accurate."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        ticket_exist = input("Enter ticket number: ")
        rows = cursor.execute(
            """SELECT EXISTS(SELECT 1 FROM flights WHERE ticket = ?)""", (ticket_exist.upper(), )
        )
        
        for row in rows:
            return row[0] == 1
        
            


