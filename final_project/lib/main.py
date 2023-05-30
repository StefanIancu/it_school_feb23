import sys
from typing import List
from abc import abstractmethod, ABC
from development import BookFlight 
from development import WhereToGo
from development import Help
from development import PlaneTicket
from development import CancelFlight
from flights_db import Database
from skeleton import DATE

class MenuItem(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def execute(self):
        pass


class MenuActionItem(MenuItem):

    def __init__(self, title, ticket):
        super.__init__(title)
        self.ticket: BookFlight = ticket
        

class FindPlane(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        try:
            demo.generate_ticket()
        except OSError as err:
            print(err)
        input("Press any key to return: ")


class MyFlights(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        try:
            Database.read_database()
        except OSError as err:
            print(err)
        input("Press any key to return: ")

class AvailableFlights(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        print(f"NOTE: Please note that the following flights are for {DATE}.")
        try:
            Database.read_flights()
        except OSError as err:
            print(err)
        input("Press any key to return: ")

class TravelTo(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        try:
            WhereToGo.see_list_of_destinations()
        except OSError as err:
            print(err)
        input("Press any key to return.")



class GiveHelp(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        try:
            Help.ask_help()
        except OSError as err:
            print(err)
        input("Press any key to return.")


class DelFlight(MenuItem):

    def execute(self):
        print(f"{self.title:-^50}\n")
        Database.read_database()
        if Database.get_ticket_existence():
            try:
                CancelFlight.delete_reservation()
            except OSError as err:
                print(err)
        else:
            print("The ticket doesn't exist.")
        input("Press any key to return.")


class MenuUserChoice(MenuItem):

    def __init__(self, title) -> None:
        super().__init__(title)
        self.__commands: List[MenuItem] = []

    def execute(self):
        user_choice = -1
        print(f"{self.title:-^50}")

        while user_choice not in range(1, len(self.__commands) + 1):
            for i, command in enumerate(self.__commands, start=1):
                print(f"{i} - {command.title}")
            try:
                user_choice = int(
                    input("Please choose an item from the list: "))
            except ValueError:
                print("Please choose an item within the range above.")

        self.__commands[user_choice - 1].execute()

    def add_choice(self, choice: MenuItem) -> None:
        self.__commands.append(choice)



class ExitItem(MenuItem):

    def execute(self):
        sys.exit(0)


demo = BookFlight("demo")


main_menu = MenuUserChoice("Welcome to FlyHome!")
main_menu.add_choice(FindPlane("Book a flight"))
main_menu.add_choice(AvailableFlights("Available flights"))
main_menu.add_choice(MyFlights("See your reservations"))
main_menu.add_choice(DelFlight("Delete a reservation"))
main_menu.add_choice(TravelTo("Where to travel"))
main_menu.add_choice(GiveHelp("Get help"))
main_menu.add_choice(ExitItem("Exit"))


while True:
    main_menu.execute()

