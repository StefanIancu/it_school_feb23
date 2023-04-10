class Shape:

    def __init__(self, color):
        print("Hello din constructor shape!")
        self.__color = color

    def set_color(self, color):
        self.__color = color

    def __str__(self) -> str:
        return f"<{__class__.__name__} color: {self.__color}>"

    #metode abstracte - inca nu e definit
    def area(self):
        pass



class Square(Shape):

    def __init__(self, length, color="red"):
        super().__init__(color)
        self.__length = length
        print("Hello din constructor square!")

    def area(self):
        return self.__length ** 2


class Triangle(Shape):
    
    def __init__(self, l1, l2, l3, color="blue"):
        super().__init__(color)
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3

    def area(self):
        return self.__l1 * self.__l2 * self.__l3



# sq1 = Square(5)
# tr1 = Triangle(5, 5, 5)

# print(sq1.area())
# print(tr1.area())

shapes = [Triangle(1, 2, 3), Triangle(2, 2, 3), Square(3), Square(4)]

for shape in shapes:
    print(shape.area())
