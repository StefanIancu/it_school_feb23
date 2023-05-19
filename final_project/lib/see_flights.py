from skeleton import FLIGHTS

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
        pass #should return to main menu


s1 = SeeFlights("See your flights")

# s1.search_flight("v2")

print(FLIGHTS)