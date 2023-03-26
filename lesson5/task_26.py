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


def power(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return power(A * A, B / 2)
    else:
        return A * power(A * A, (B - 1) / 2)


input_a = tm.recurse_input_natural(f"Введите значение основания степени: ")
input_b = tm.recurse_input_natural("Введите значение показателя степени: ")
tm.output_dynamic_string(f'{input_a}^{input_b} = {power(input_a, input_b)}')
