__author__ = 'Alex Bulavin'
"""
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
import os
import random
from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True


def an_element(a, n, d, counter):
    print(f"a{counter} = {a + (counter) * d}")
    counter += 1
    if counter <= n:
        return an_element(a, n, d, counter)
    return 


input_a1 = tm.input_any_int(f"Введите первый элемент прогрессии: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)

input_d = tm.input_any_int("Введите разность прогрессии: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)

input_n = tm.input_any_int("Введите количество элементов прогрессии: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)

an_element(input_a1, input_n, input_d, 1)
