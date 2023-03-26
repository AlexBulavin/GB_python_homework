__author__ = 'Alex Bulavin'
"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
a[n] = -a[n-1]/2
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
import os

from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True  #  На время отладки выставляем флаг в True
start_number = 1  # Ряд начинается с 1


def sum_calc(self, counter, sum_num):
    if counter > 1:
        print(f"def sum_calc self = {self}, counter = {counter}, "
              f"sum_num = {sum_num}"
              if (debug_mode) else "")
        self /= -2
        counter -= 1
        sum_num += self
        return sum_calc(self, counter, sum_num)
    else:
        return sum_num


#  Main algorithm
input_number = tm.recurse_input_natural(f"Введите количество элементов: ",
                                        NOT_INT_POSITIVE_OR_TEXT, debug_mode)
print(f"Количество элементов ряда a[n] = -a[n-1]/2 равно {input_number}"
      f", их сумма: {sum_calc(start_number, input_number, start_number)}")

