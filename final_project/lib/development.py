import csv
import random
from string import ascii_uppercase
from string import punctuation
import sqlite3
from datetime import date
from pathlib import Path

from fpdf import FPDF
from skeleton import DESTINATIONS_AND_PRICES
from skeleton import FROM as airport
from skeleton import GATE
from skeleton import DATE
from skeleton import ROOT



DB_PATH = ROOT / "flights.db"
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

class BookFlight:

    current_price = 0

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    def get_user_name(self):
        """Takes the user's name."""
        while True:
            name_answer = input("What is your name?")
            if any(i.isdigit() for i in name_answer):
                print("Please enter the correct name without numbers.")
            elif any(i for i in name_answer if i in punctuation):
                print("Please don't use characters.")
            elif name_answer == "":
                print("Field required.")
            else:
                break
        print(f"Welcome, {name_answer.title()}!")
        return name_answer.title()

    def get_user_destination(self):
        """Takes the user destination and matches the starting price of the
        ticket with the specific destination price from DESTINATIONS_AND_PRICES
        dictionary. This can be changed anytime."""
        while True:
            destination_answer = input(f"Where would you like to go? ")
            if destination_answer.lower() in list(DESTINATIONS_AND_PRICES.keys()):
                PlaneTicket.current_price += DESTINATIONS_AND_PRICES[destination_answer.lower()]
                Database.read_flights(destination_answer)
                break
            else:
                print("We are sorry. We currently don't fly there!")
        return destination_answer


    def pick_a_flight(self):
        while True:
            flight_answer = input("Please choose a flight by entering its number: ")
            if Database.read_numbers(flight_answer.upper()):
                break
            else:
                print("Please enter the correct flight number.")
        return flight_answer

    def get_user_seat(self):
        """Asks the user if they would like to book a seat or not. If the user
        replies positively, the current price will increase."""
        while True:
            seat_answer = input("Would you like to reserve a seat? [y/n]")
            if seat_answer in "yesYES":
                PlaneTicket.current_price += 50
                seat_answer = (
                    f"{random.choice(range(75))}{random.choice(ascii_uppercase)}"
                )
                break
            elif seat_answer in "noNO":
                seat_answer = "(to be assigned at check-in)"
                break
            else:
                print("Sorry, not an answer.")
        return seat_answer

    def get_user_luggage(self):
        """Asks the user if they would like to book a luggage. If the user
        replies positively, the current price will increase."""
        while True:
            luggage_answer = input("Would you like to book a luggage? [y/n]")
            if luggage_answer in "yesYES":
                PlaneTicket.current_price += 50
                break
            elif luggage_answer in "noNO":
                break
            else:
                print("Sorry, that's not an answer.")
        return luggage_answer

    def get_user_date(self):
        """Asks the user the date (day) when they would like to fly.
        This is combined with the DATE constant which is the current month of
        the year - based on real date&time."""
        while True:
            user_date = input(f"When would you like to fly? [day.{DATE}]")
            if user_date.isdigit():
                user_date = int(user_date)
                if 0 < user_date <= 31:
                    break
                else:
                    print("Date must be between 1 and 31.")
            else:
                print("Please enter a valid format [day].")
        return user_date


    def generate_ticket(self):
        """Main method that takes all the information together and generates
        an object - ticket. It also adds the ticket's number to the "flights"
        database."""
        PlaneTicket.current_price = 0
        name = self.get_user_name()
        WhereToGo.see_list_of_destinations()
        destination = self.get_user_destination()
        flight = self.pick_a_flight()
        seat = self.get_user_seat()
        luggage = self.get_user_luggage()
        date = self.get_user_date()
        price = PlaneTicket.current_price
        print("Your ticket has been generated. Thank you for picking us!")
        Database.drop_seats(flight.upper())
        ticket = PlaneTicket(PlaneTicket.number, name, seat, date, destination, flight)
        number = ticket.number
        self.generate_pdf(ticket.number, seat, name, destination, date, flight)
        cursor.execute(
            """INSERT INTO flights ("name", "destination", "cost", "ticket") VALUES (?, ?, ?, ?)""",
            (name, destination.title(), price, number)
        )
        connection.commit()
       
    def generate_pdf(self, number, seat, name, destination, date, flight_number):
        """Method that takes some user information and fills a PDF file
        with the specific information."""
        pdf = FPDF()
        pdf.add_page(orientation="l")
        pdf.set_font("Arial", size=15)
        pdf.cell(40, 10, border =1, txt=f"Ticket no: {number} ", ln=1)
        pdf.cell(270, 10, txt="FlyHome", ln=1, align="R")
        pdf.cell(250, 20, txt="BOARDING PASS", ln=2, align="C")

        pdf.cell(52, 10, txt=f"Mr./Mrs. {name} ", ln=3, align="L")
        pdf.cell(150, 10, txt=f"Seat number: {seat}", ln=4, align="L")
        pdf.cell(150, 10, txt=f"Flight number: {flight_number.upper()}", ln=4, align="L")


        pdf.cell(270, 10, txt=f"Departure date: {date}.{DATE}", ln=7, align="R")
        pdf.cell(270, 10, txt=f"Gate: {GATE}", ln=8, align="R")
        pdf.cell(270, 10, txt=f"From: {airport}", ln=9, align="R")
        pdf.cell(270, 10, txt=f"To: {destination.title()}", ln=10, align="R")
        pdf.image("airplane.jpeg", w=10, h=10, x=235, y=100)

        pdf.cell(100, 10, txt="Gate closes 15 minutes before departure.",
                 ln = 11, align="L") 
        pdf.cell(
            100, 10, txt="Thank you for choosing to fly with us!", ln=12, align="L"
        )
        pdf.cell(100, 10, txt = "More details at: www.flyhome.com",
                 ln = 13, align= "L")
        
        pdf.image("plane.jpeg", w=60, h=60, x=190, y=1)
        pdf.code39("*fpdf2*", x=130, y=140, w=4, h=15)

        pdf.cell(100, 10, txt="*Please watch screens for border time.",
                 ln=21, align="L")
        pdf.cell(100, 10, txt="**No refund available for this flight.",
                 ln=22, align="")
        
        pdf.output(f"planeticket_{number}.pdf")


class WhereToGo:

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @staticmethod
    def see_list_of_destinations():
        """Reads the destinations available and their prices from a csv file."""
        with open("destinations.csv") as fin:
            reader = csv.reader(fin.readlines()[1:])

        for line in reader:
            # print(f"{line[0]} €{line[1]}")
            # print(line[0].split(";"))
            print(f"""{line[0].replace(";", " from €")}""")


class Help:
    
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @staticmethod
    def ask_help():
        """Provides useful information to the user."""
        with open(ROOT / "travel.txt", "r") as fin:
            content = fin.readlines()
  
        for line in content:
            print(line.strip(" \n\r\t"))



class CancelFlight:

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @staticmethod
    def delete_reservation():
        """Deletes a reservation booked by the user."""
        while True:
            del_res = input("Please enter your ticket number to delete the reservation: ")
            if Database.get_ticket_existence(del_res.upper()):
                cursor.execute(
                    """DELETE FROM flights WHERE ticket == ?""", (del_res.upper(), )
                )
                connection.commit()
                print(f"The reservation with {del_res.upper()} has been successfully deleted. ")
                break
            else:
                print(f"Ticket {del_res.upper()} doesn't exist.")




class PlaneTicket(BookFlight):

    current_number = 100

    def __init__(self, number, name: str, seat, date, destination, flight_number):
        self.__number = f"{random.choice(ascii_uppercase)}{PlaneTicket.current_number}"
        self.__name = name
        self.__seat = seat
        self.__date = date
        self.__destination = destination
        self.__flight_number = flight_number
        PlaneTicket.current_number += 1
        self.current_price = 0

    @property
    def name(self):
        return self.__name    
    
    @property
    def number(self):
        return self.__number
    
    @property
    def seat(self):
        return self.__seat
    
    @property
    def date(self):
        return self.__date
    
    @property
    def flight_number(self):
        return self.__flight_number

    @property
    def destination(self):
        if self.__destination not in list(DESTINATIONS_AND_PRICES.keys()):
            print(f"Destination not in {DESTINATIONS_AND_PRICES}.")
        return self.__destination
    

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
    def read_flights(destination):
        """Method that reads from a database of flights a specific destination
        which the user chooses - method for "BOOK A FLIGHT OPTION" where it 
        needs an argument - user input."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        while True:
            # destination = input("What destination interests you? ")
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
    def read_flights_for_available():
        """Method that reads from a database of flights a specific destination
        which the user chooses - method for "AVAILABLE FLIGHTS" option where it 
        is static, doesn't need any arguments."""
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
    def read_numbers(flight_number):
        """Method that reads from a database of flights certain flights numbers."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        rows = cursor.execute(
            """SELECT EXISTS(SELECT 1 FROM departures WHERE flight_number = ?)""", (flight_number.upper(), )
        )
        
        for row in rows:
            return row[0] == 1


    @staticmethod
    def get_ticket_existence(ticket):
        """Method that returns bool if a specific ticket is in flights database
        in order to help the delete_reservation method to be accurate."""
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        rows = cursor.execute(
            """SELECT EXISTS(SELECT 1 FROM flights WHERE ticket = ?)""", (ticket.upper(), )
        )
        
        for row in rows:
            return row[0] == 1
    
    @staticmethod
    def drop_seats(flight_number):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        rows = cursor.execute(
            """UPDATE departures 
            SET "seats " = "seats " - 1 
            WHERE "flight_number" == ? """, (flight_number, )
        )
        connection.commit()

    # @staticmethod
    # def check_seats(flight_number):
    #     connection = sqlite3.connect(DB_PATH)
    #     cursor = connection.cursor()
    #     rows = cursor.execute(
    #         """SELECT "seats " from departures WHERE "flight_number" == ?""", (flight_number, )
    #     )
    #     for row in rows:
    #         return row[0]
        