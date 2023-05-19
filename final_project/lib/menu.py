import sys
from typing import List
from abc import abstractmethod, ABC
from booking_a_flight import BookFlight

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
        

class ExitItem(MenuItem):

    def execute(self):
        sys.exit(0)