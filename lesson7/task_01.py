__author__ = 'Alex Bulavin'
'''
Задание 1.

Создать класс TrafficLight (светофор) и определить у него один приватный 
атрибут color (цвет) и публичный метод running (запуск). 

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import os
from time import sleep
from ..lesson3.library import bcolors

os.environ['TERM'] = 'xterm'
# Очищаем консоль
os.system('clear')


debug_mode = False  # True


class TrafficLight:
    def __init__(self):
        self.__color = {"КРАСНЫЙ": 7, "ЖЕЛТЫЙ": 2, "ЗЕЛЕНЫЙ": 5}

    def running(self):
        """
        Метод "переключает" светофор
        красный - 7 секунд
        желтый - 2 секунды
        зеленый - 5 секунд
        """
        while True:
            for k, v in self.__color.items():
                if k == "КРАСНЫЙ":
                    prt_color = bcolors.CRED
                elif k == "ЖЕЛТЫЙ":
                    prt_color = bcolors.CYELLOW
                else:
                    prt_color = bcolors.CGREEN
                for i in range(v, 0, -1):
                    print(f'\rСейчас горит', prt_color, bcolors.CSELECTED,
                          f'{k} ', end="")
                    print(bcolors.CEND, f' цвет светофора ',
                          f'{i}', end="")
                    sleep(1)


traffic_light1 = TrafficLight()
traffic_light1.running()
