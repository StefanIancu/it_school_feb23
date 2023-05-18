from book_flight import BookFlight

class Menu(BookFlight):

    def __init__(self):
        self

    def book_a_flight(self):
        return BookFlight.title
    

m1 = Menu()

print(m1.book_a_flight())
