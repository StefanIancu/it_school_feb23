from skeleton import DESTINATIONS_AND_PRICES
from skeleton import FLIGHTS
import random
from string import ascii_uppercase
from fpdf import FPDF
from skeleton import FROM as airport
from skeleton import GATE 
from qrcode import QRCode
from skeleton import MONTH

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
        """Takes the user destination."""
        while True:
            destination_answer = input(f"Welcome, user. Where would you like to go?")
            if destination_answer.lower() in list(DESTINATIONS_AND_PRICES.keys()):
                BookFlight.current_price += DESTINATIONS_AND_PRICES[destination_answer]
                break
            else:
                print("We are sorry. We currently don't fly there!")
        return destination_answer
        
    
    def get_user_seat(self):
        """Asks the user if they would like to book a seat or not."""
        while True:
            seat_answer = input("Would you like to reserve a seat? [y/n]")
            if seat_answer in "yesYES":
                BookFlight.current_price += 50
                seat_answer = f"{random.choice(range(126))}{random.choice(ascii_uppercase)}"
                break 
            elif seat_answer in "noNO":
                break
            else:
                print("Sorry, not an answer.")
        return seat_answer
    
    def get_user_luggage(self):
        """Asks the user if they would like to book a luggage."""
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
            user_date = input("When would you like to fly? [day]")
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
        a ticket."""
        name = self.get_user_name()
        destination = self.get_user_destination()
        seat = self.get_user_seat()
        luggage = self.get_user_luggage()
        date = self.get_user_date()
        self.generate_pdf(seat, name, destination, date)
        print("Your ticket has been generated. Thank you for picking us!")

    def generate_pdf(self, seat, name, destination, date):
        """Method that takes some usor information and fills a PDF file
        with the specific information."""
        pdf = FPDF()
        pdf.add_page(orientation="L")
        pdf.set_font("Arial", size = 15)
        pdf.cell(180, 10, txt=f"Ticket no: ",
            ln = 1)
        pdf.cell(200, 10, txt = "BOARDING PASS",
            ln = 2, align= "C")


        pdf.cell(200, 10, txt = f"Mr./Mrs. {name} ",
            ln = 3, align= "L")
        
        pdf.cell(150, 10, txt=f"Seat number: {seat}",
            ln = 4, align="L")
        
        pdf.cell(150, 10, txt=f"Departure date: {date}.{MONTH}",
            ln = 7, align = "R")
        pdf.cell(150, 10, txt=f"Gate: {GATE}",
            ln = 8, align = "R")
        pdf.cell(150, 10, txt=f"From: {airport}",
            ln = 9, align = "R")
        pdf.cell(150, 10, txt=f"To: {destination.title()}",
            ln = 10, align = "R")
        

        pdf.cell(100, 10, txt="Thank you for choosing to fly with us!",
            ln = 11, align="C")
        
        # pdf.image("plane.jpeg", w=40, h=40)
        
        # pdf.code39("*fpdf2*", x=30, y=50, w=4, h=20,)

        pdf.output("planeticket.pdf")


book = BookFlight("Where do you want to go?")


# book.generate_pdf()

print(f"Your current cost is ${book.current_price}.")
book.generate_ticket()
print(f"Your total cost with taxes is ${book.current_price}.")

