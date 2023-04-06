__author__ = 'Alex Bulavin'
'''
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
'''


class Road:
    def __init__(self, len_and_width):
        self._len_and_width = len_and_width
        self.density = 25
        self.thickness = 0.05

    def atphalt_mass(self):
        massa = self._len_and_width[0] \
                * self._len_and_width[1] \
                * self.thickness * self.density
        print(f"Для покрытия дорожного полотна длиной "
              f"{self._len_and_width[0]} метров, шириной "
              f"{self._len_and_width[1]} метров, толщиной "
              f"{int(self.thickness * 100)} см. необходимо "
              f"{int(massa)} кг = {massa / 1000}т асфальтобетонной смеси")


road1 = Road([5000, 20])
road1.atphalt_mass()
