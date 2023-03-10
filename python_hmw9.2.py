"""
Создать метакласс для паттерна Синглтон """


class Cloner(type):
    link = 0

    def __call__(self, *args):
        if (self.link == 0):
            self.link = type.__call__(self, *args)
        return self.link


class Dolly(metaclass=Cloner):
    animal_type = "sheep"

    def __init__(self):
        print("Это настоящая овца!")


animal1 = Dolly()
animal2 = Dolly()
animal3 = Dolly()
print(animal1 == animal2 == animal3)
