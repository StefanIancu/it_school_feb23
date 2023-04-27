class Bill:

    current_number = 1
    
    def __init__(self, valoare_totala) -> None:
       self.__numar = Bill.current_number
       self.valoare_totala = valoare_totala
       Bill.current_number += 1


    @property
    def numar(self):
        return self.__numar


f1 = Bill(100)
f2 = Bill(20)

print(f1.numar)
print(f2.numar)

