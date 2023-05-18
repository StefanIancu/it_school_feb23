from skeleton import DESTINATIONS_AND_PRICES

class BookFlight:

    current_price = 0

    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title
    
    def get_user_destination(self):
        while True:
            destination_answer = input("Where would you like to go?")
            if destination_answer.lower() in list(DESTINATIONS_AND_PRICES.keys()):
                BookFlight.current_price += DESTINATIONS_AND_PRICES[destination_answer]
                break
            else:
                print("We are sorry. We currently don't fly there!")
        return destination_answer
        
    
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

    def generate_ticket(self):
        self.get_user_destination()
        self.get_user_seat()
        self.get_user_luggage()
        self.get_user_date()



book = BookFlight("john")




# print(book.current_price)
# book.generate_ticket()
# print(book.current_price)