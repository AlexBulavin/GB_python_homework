__author__ = 'Alex Bulavin'
"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*

2 2
    4 

"""
import os
import random
from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True


def sum_a_b(a, b):
    if b == 0:
        return a
    else:
        return sum_a_b(a + 1, b - 1)


input_a = tm.recurse_input_natural(f"Введите первое слагаемое: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
input_b = tm.recurse_input_natural("Введите второе слагаемое: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
tm.output_dynamic_string(f'{input_a}+{input_b} = '
                         f'{sum_a_b(input_a, input_b)}\n')

