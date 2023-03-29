__author__ = 'Alex Bulavin'
"""
Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного 
максимума)

После загрузки задания, вы можете проверить себя самостоятельно с помощью 
эталонного решения
"""
import os
import random
from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True

input_data_min = tm.input_any_int(f"Введите минимальное значение элемента "
                                  f"списка: ",
                                  NOT_INT_POSITIVE_OR_TEXT, debug_mode)
input_data_max = tm.input_any_int(f"Введите максимальное значение "
                                  f"элемента списка: ",
                                  NOT_INT_POSITIVE_OR_TEXT, debug_mode)
data_list = []
tm.list_fill_random_int(data_list, 10, 0, 100, True, True, "data_list", False)
data_list.sort()
print(f"Отсортированный список: ", * data_list)
print(f"Индексы элементов, которые >= {input_data_min} и <= {input_data_max}")
print(*list(i for i in range(len(data_list))
            if input_data_max >= data_list[i] >= input_data_min))
