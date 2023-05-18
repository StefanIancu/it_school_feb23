from pathlib import Path

ROOT = Path(__file__).parent
DESTINATIONS_AND_PRICES = {
                "bucharest": 150, "budapest": 150, "bratislava": 165, 
                "sofia": 150, "prague": 200, "berlin": 250, "rome": 400,
                "paris": 350, "basel": 550, "tokyo": 999 
                }

class PlaneTicket:

    current_number = 100

    def __init__(self, number, name: str, seat: int, date: str, destination: str):
        self.__number = PlaneTicket.current_number
        self.__name = name
        self.__seat = seat
        self.__date = date
        self.__destination = destination
        PlaneTicket.current_number += 1

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
    def destination(self):
        if self.__destination.lower not in DESTINATIONS_AND_PRICES:
            print(f"Destination not in {DESTINATIONS_AND_PRICES}.")
        return self.__destination

ticket = PlaneTicket(1, "Stefan Iancu", 45, "15.07.2023", "Budapest")
ticket2 = PlaneTicket(1, "Daniel Gheorghe", 46, "11.07.2023", "Rome")
ticket3 = PlaneTicket(1, "Andreea Savu", 47, "19.07.2023", "Tokyo")


class BookFlight:

    current_price = 0

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title
    
    def get_user_destination(self):
        while True:
            user_destination = input("Where would you like to go?")
            if user_destination.lower not in DESTINATIONS_AND_PRICES:
                print("Sorry, currently we don't fly there!")
            else:
                break
        return user_destination
    
    def get_user_seat(self):
        while True:
            seat_answer = input("Would you like to reserve a seat? [y/n]")
            if seat_answer in "yesYES":
                BookFlight.current_price += 50
                break 
            elif seat_answer in "noNO":
                break
            else:
                print("Sorry, not an answer.")
        return seat_answer
    
    def get_user_luggage(self):
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

    # def generate_ticket(self):



# book = BookFlight("jhon")

# book.get_user_destination()

