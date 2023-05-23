import csv
import random
from string import ascii_uppercase

from fpdf import FPDF
from skeleton import DESTINATIONS_AND_PRICES, FLIGHTS
from skeleton import FROM as airport
from skeleton import GATE, MONTH
from skeleton import FLIGHTS
from ticket import PlaneTicket


class BookFlight:

    current_price = 0

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    def get_user_name(self):
        """Takes the user's name."""
        name_answer = input("What is your name?")
        return name_answer

    def get_user_destination(self):
        """Takes the user destination and matches the starting price of the
        ticket with the specific destination price from DESTINATIONS_AND_PRICES
        constant. This can be changed anytime."""
        while True:
            destination_answer = input(f"Welcome, user. Where would you like to go?")
            if destination_answer.lower() in list(DESTINATIONS_AND_PRICES.keys()):
                BookFlight.current_price += DESTINATIONS_AND_PRICES[destination_answer]
                break
            else:
                print("We are sorry. We currently don't fly there!")
        return destination_answer

    def get_user_seat(self):
        """Asks the user if they would like to book a seat or not. If the user
        replies positively, the current price will increase."""
        while True:
            seat_answer = input("Would you like to reserve a seat? [y/n]")
            if seat_answer in "yesYES":
                BookFlight.current_price += 50
                seat_answer = (
                    f"{random.choice(range(126))}{random.choice(ascii_uppercase)}"
                )
                break
            elif seat_answer in "noNO":
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
                BookFlight.current_price += 50
                break
            elif luggage_answer in "noNO":
                break
            else:
                print("Sorry, that's not an answer.")
        return luggage_answer

    def get_user_date(self):
        """Asks the user the date (day) when they would like to fly.
        This is combined with the MONTH constant which is the current month of
        the year. The constant can be changed anytime."""
        while True:
            user_date = input(f"When would you like to fly? [day.{MONTH}]")
            if user_date.isdigit():
                user_date = int(user_date)
                if user_date > 0:
                    break
                else:
                    print("Date must be greater than 0.")
            else:
                print("Please enter a valid format [day].")
        return user_date


    def generate_ticket(self):
        """Main method that takes all the information together and generates
        an object - ticket. It also adds the ticket's number to the FLIGHTS list."""
        name = self.get_user_name()
        destination = self.get_user_destination()
        seat = self.get_user_seat()
        luggage = self.get_user_luggage()
        date = self.get_user_date()
        print("Your ticket has been generated. Thank you for picking us!")
        ticket = PlaneTicket(PlaneTicket.number, name, seat, date, destination)
        FLIGHTS.append(ticket.number)
        number = ticket.number
        self.generate_pdf(ticket.number, seat, name, destination, date)

    def generate_pdf(self, number, seat, name, destination, date):
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

        pdf.cell(270, 10, txt=f"Departure date: {date}.{MONTH}", ln=7, align="R")
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
        
        pdf.output("planeticket.pdf")



class SeeFlights:

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    def search_flight(self, number: str):
        """Asks users the ticket number and searches the number in the list
        of FLIGHTS constant. The list updates with every ticket generated."""
        if number in FLIGHTS:
            print("Flight found!")
        else:
            print("There are no flights matching the criteria.")

    def go_back(self):
        pass  # should return to main menu


class WhereToGo:

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    def see_list_of_destinations(self):
        print("List of destinations")
        with open("destinations.csv") as fin:
            reader = csv.reader(fin.readlines())

        for line in reader:
            print(line[0])

    def download_brochure(self):
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=15)

        pdf.cell(200, 10, txt="BROCHURE", ln=1, align="C")

        pdf.cell(150, 10, txt=f"reader", ln=2, align="R")

        # for k, v in DESTINATIONS_AND_PRICES.items():
        #     pdf.cell(150, 10, txt=f"To {k.title}, price ${v}",
        #              ln=2.)

        # pdf.cell(200, 10, txt = f"Mr./Mrs. {ticket.name}",
        #  ln = 3, align= "L")
        # pdf.cell(150, 10, txt=f"Seat number: {ticket.seat}",
        #  ln = 4, align="L")

        # pdf.cell(150, 10, txt=f"Departure date: {ticket.date}",
        #  ln = 5, align="R")
        # pdf.cell(150, 10, txt=f"Destination: {ticket.destination}",
        #  ln = 6, align="R")

        pdf.cell(
            100, 10, txt="Thank you for choosing to fly with us!", ln=10, align="C"
        )

        pdf.output("planeticket.pdf")


class Help:
    
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    # TBA

demo = BookFlight("demo")

print(FLIGHTS)

demo.generate_ticket()

print(FLIGHTS)
