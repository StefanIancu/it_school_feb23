from dataclasses import dataclass, field
from random import randint
from uuid import uuid4, UUID

class Car:

    def __init__(self, tank, doors):
        self.tank_capacity = tank
        self.doors = doors
        self.gas = 0

@dataclass
class Ship:
    id: UUID = field(init=False, default_factory=uuid4)
    tank_capacity: int
    fuel: int
    seats: int = field(init=False, default_factory= lambda: randint(1, 22))  #nu e inclus in constructor 





ford = Car(55, 4)
boat = Ship(50, 40)
boat1 = Ship(20, 23)

print(ford)
print(boat)
print(boat1)