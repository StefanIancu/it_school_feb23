class Person:

    def __init__(self):
        self.__height = 170
        self.__weight = 70


    def get_cm_height(self):
        return self.__height
    
    def get_m_height(self):
        return self.__height / 100


stefan = Person()
andreea = Person()


print(f"Inaltimea in cm este: {stefan.get_cm_height()}")
print(f"Inaltimea in m este: {stefan.get_m_height()}")