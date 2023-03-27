__author__ = 'Alex Bulavin'
"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 

"""
import os
import random
from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


input_a = tm.recurse_input_natural(f"Введите значение основания степени: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
input_b = tm.recurse_input_natural("Введите значение показателя степени: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
tm.output_dynamic_string(f'{input_a}^{input_b} = {power(input_a, input_b)}\n')
