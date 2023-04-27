class Car:

    sound = "ta ta ta"

    def __init__(self) -> None:
        self.__engine_started = False
        #Car.horn() metoda statica se poate apela si in metoda de instanta

    def start_engine(self):
        self.__engine_started = True

    def stop_engine(self):
        self.__engine_started = False

    @staticmethod
    def horn():
        print(Car.sound)



#Client Code
vw = Car()
# vw.horn()
Car.horn()

