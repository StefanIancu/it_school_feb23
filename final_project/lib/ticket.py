from booking_a_flight import BookFlight
from skeleton import FLIGHTS
import random
from string import ascii_uppercase
from skeleton import DESTINATIONS_AND_PRICES

class PlaneTicket(BookFlight):

    current_number = 100

    def __init__(self, number, name: str, seat, date, destination):
        self.__number = f"{random.choice(ascii_uppercase)}{PlaneTicket.current_number}"
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
        if self.__destination not in list(DESTINATIONS_AND_PRICES.keys()):
            print(f"Destination not in {DESTINATIONS_AND_PRICES}.")
        return self.__destination

# ticket = PlaneTicket(1, "Stefan Iancu", 45, "15.07.2023", "Budapest")
# ticket2 = PlaneTicket(1, "Daniel Gheorghe", 46, "11.07.2023", "Rome")
# ticket3 = PlaneTicket(1, "Andreea Savu", 47, "19.07.2023", "Tokyo")


# print(FLIGHTS)


# def match_a_ticket():
