class Laptop:

    @staticmethod
    def beep():
        print("sssss")



class PC:

    #metoda statica - se poate ajunge la ea prin clasa
    @staticmethod
    def beep():
        print("trrrr")


PC.beep()
Laptop.beep()

