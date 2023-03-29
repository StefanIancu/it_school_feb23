class Car:
    """Representation of a virtual car."""

    def __init__(self):                                             #constructor//va fi executat la fiecare instantiere
        self.__cmc = 3000
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 20
        self.__passengers = []
        self.__engine_running = True

    def get_engine_running(self):
        """Check if engine is running or not."""
        if self.__engine_running == True:
            return(f"Engine already running!")
        else:
            return(f"Engine is off.")

    def start_engine(self):
        if self.__engine_running == False:
            print("Please start the engine!")
        if self.__engine_running == True:
            raise RuntimeWarning("Engine already running!")

    def stop_engine(self):
        if self.__engine_running == True:
            return(f"Press Stop to stop the engine.")
        if self.__engine_running == False:
            raise TimeoutError("Engine off.")
            

    def drive(self, km):
        """1. verifica daca motorul functioneaza, daca nu exceptie
        2. verifici daca poti parcurge km, daca nu ai combustibil ridici exceptie
        3. daca ai combustibil sa parcurgi km, trebuie consumat conbustibilul 
        - consuml per km se calculeaza ca fiind __cmc / 1000"""
        if self.__gas_in_tank <= 1:
            raise ValueError("Fuel level low. Please refuel!")
        else:
            print("Welcome, have a good trip!")
            consum_per_km = self.__cmc / 1000
            gas_to_burn = (consum_per_km * km) - self.__gas_in_tank
            return (f"Your estimated gas to burn is: {gas_to_burn} litres!")

    def refill(self, litres):
        if litres > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow!")
        self.__gas_in_tank = litres

    def get_doors(self):
        return self.__doors

    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 100



vw = Car()
ford = Car()
# print(f"Combustibil ramas {vw.get_gas_percentage()} %")
# vw.refill(33)
# print(f"Combustibil ramas {vw.get_gas_percentage()} %")

# print(vw.get_engine_running())
# print(vw.start_engine())
# print(vw.stop_engine())
print(vw.drive(10))
# print(vw.get_engine_running())
#  print(f"CMC VW: {vw.cmc}")
# print(f"CMC Ford: {ford.cmc}")

# # vw.__cmc = 3000

# print(f"CMC VW: {vw.__cmc}")
# print(f"CMC Ford: {ford.__cmc}")


# print(vw.get_doors())

# print(f"Combustibil ramas {vw.get_gas_percentage()} %")


