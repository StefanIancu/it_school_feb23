import see_flights
import ticket
from booking_a_flight import BookFlight
import skeleton


class Menu:

    def __init__(self, title):
        self.title = title

    def execute(self):
        print(f"{self.title}.")


class RezervaZbor(BookFlight):

    def __init__(self, title):
        self.__title = title

    def execute(self):
        while True:
            print("""
            1. Rezerva zbor
            2. Gaseste zbor
            3. Vezi destinatii
            4. Ajutor
            """)
            choice = input("Choose an item: ")
            if choice.isdigit():
                choice = int(choice)
                if choice is 1:
                    print("Execut 1")
                    break
                elif choice is 2:
                    print("Execut 2")
                    break
                elif choice is 3:
                    print("Execut 3")
                    break
                elif choice is 4: 
                    print("Execut 4")
                    break
                else:
                    print("Please choose an item from the ones below.")
            else:
                print("Please choose a number.")
        return choice 
        


class VerificaBilet(Menu):

    def __init__(self, title):
        self.title = title

    def execute(self):
        print(f"{self.title}")


menu_title = Menu("Welcome to AirFlight!")
menu_item2 = RezervaZbor("1. Book a flight!")
menu_item3 = VerificaBilet("2. Check your tickets.")

menu_item2.execute()