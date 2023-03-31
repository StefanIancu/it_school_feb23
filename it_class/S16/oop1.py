from autos import Car
from users import Person
from autos import GasStation

gas1 = GasStation(1234)
gas1.set_price(6.55, 1234)
# print(gas1.get_price())

vw = Car()
ford = Car()

print(ford.get_gas_percentage())

print(gas1.fill(ford, 10))

print(ford.get_gas_percentage())

print(ford.ready_for_fill())




vlad = Person()
maria = Person()

vw = Car()
ford = Car()

# print(ford.get_gas_percentage())
# ford.get_consumption()
# ford.start_engine()
# ford.refill(16)
# ford.drive(1)

# print(ford.get_consumption())

# ford.add_person(vlad)
# ford.add_person(maria)

# print(ford.get_consumption())

