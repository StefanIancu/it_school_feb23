class ElectricVehicle:

    def charge(self):
        print("Charging")

class DieselVehicle:

    def refill(self):
        print("Refilling")


class HybridVehicle(ElectricVehicle, DieselVehicle):
    pass


toyota = HybridVehicle()

toyota.charge()
toyota.refill()