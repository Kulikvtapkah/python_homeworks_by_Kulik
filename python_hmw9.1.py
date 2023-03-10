"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

"""


class RealNumber:

    def __set__(self, instance, value):
        if (type(value) == int or type(value) == float):
            if value <= 0:
                raise ValueError("Значение должно быть положительным")
            instance.__dict__[self.my_attr] = value
        else:
            raise TypeError("Значение должно быть числом")

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    # Четыре дескриптора:
    thickness = RealNumber()
    _length = RealNumber()
    _width = RealNumber()
    density = RealNumber()

    def __init__(self, _width, _length, density=2.75, thickness=0.07):
        self._length = _length
        self._width = _width
        self.density = density
        self.thickness = thickness

        print(f"Покрытие из асфальтобетона {self._width}х{self._length} м2."
              f" Плотность по умолчанию: {self.density} т/м3, толщина по умолчанию: {self.thickness}м. ")

    def mass_calculation(self):
        mass = self.thickness * self.density * self._length * self._width
        print(f"Для покрытия {self._width}х{self._length} м2,"
              f" плотностью {self.density} т/м3, толщиной {self.thickness} м "
              f"масса асфальтобетона = {mass} т.")
        return mass


my_road = Road(9, 1000)
my_road.density = 2.3
my_road.thickness = 0.08
m = my_road.mass_calculation()
print(f"\nУра, теперь я могу использовать массу моей дороги! Например, масса трех таких дорог = {3 * m} т))")
