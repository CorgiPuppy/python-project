# Internal and private variables
class Car:
    def __init__(self):
        self._color = "yellow"
        self.__model = "bmw"

car = Car()
print(car._color)
print(dir(car))
print(car._Car__model)