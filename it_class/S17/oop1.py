from typing import Self

s1 = "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"
CARD_SYMBOLS =["♠", "♥", "♦", "♣"]
CARD_VALUE_MAP = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "A" : 11,
    "J" : 12,
    "Q" : 13,
    "K" : 14,
}






class Card:

    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number.")
        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol.")
        self.__symbol = symbol
        self.__number = number

    def __str__(self) -> str:
        # trebuie sa returneze string
        return f"{self.__number}{self.__symbol}"
    
    def __repr__(self) -> str:
        return self.__str__()
    

    def get_number(self) -> int:
        return CARD_VALUE_MAP[self.__number]
    
    def get_symbol(self) -> str:
        return self.__symbol
    

    #__lt__ <
    #__le__ <=
    #__gt__ >
    #__ge__ >=
    def __lt__(self, other):
        return self.get_number() < other.get_number()
    
    def __le__(self, other):
        return self.get_number() <= other.get_number()
    
    def __gt__(self, other):
        return self.get_number() > other.get_number()
    
    def __ge__(self, other):
        return self.get_number() >= other.get_number()
    
    def __add__(self, other) -> int:
        #returneaza acelasi tip, dar obiect nou 
        return self.get_number() + other.get_number()
    
    def __eq__(self, other):
        # operator overloading
        # returneaza boolean 
        # if self.number == other.number:
        #     if self.symbol == other.symbol:
        #         return True
        # return False
        return self.__number == other.get_number() and self.__symbol == other.get_symbol()

    

class Deck:

    def __init__(self) -> None:
        self.__cards = []
        for v in CARD_VALUE_MAP:
            for s in CARD_SYMBOLS:
                self.__cards.append(Card(v, s))
        self.__current_card = len(self.__cards) - 1

    # def get_size(self):
    #     return len(self.__cards)

    def __len__(self):
        #trebuie sa returneze int sau float
        return len(self.__cards)
    
    def __iter__(self):
        self.__current_card = len(self.__cards) - 1
        return self
    
    def __next__(self):
        if self.__current_card == -1:
            raise StopIteration()
        cc = self.__cards[self.__current_card]
        self.__current_card -= 1
        return cc
    
    def __reversed__(self):
        return reversed(self.__cards)

    def get_value(self):
        return CARD_VALUE_MAP  #to be continued


d1 = Deck()


c1 = Card("A", CARD_SYMBOLS[0])
c2 = Card("2", CARD_SYMBOLS[1])


# print(f"Carti in pachet: {len(d1)}")

# print(c1 > c2)
# print(c1 >= c2)
# print(c1 < c2)
# print(c1 <= c2)

# print(c1)


d1_iter = iter(d1)

# print(next(d1))

# for i in d1:
#     print(i)


def septica(deck:Deck):
    for card in deck:
        if card.get_value() >= 7:
            yield card

d1.shuffle()
septica_cards = septica(d1)

for i in septica_cards:
    print(i)