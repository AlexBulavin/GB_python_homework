__author__ = 'Alex Bulavin'

import os

from library import TypicalMethods as tm
from strings_const import *
from library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True  #  На время отладки выставляем флаг в True
digits_list = []


def number_reverser(self, input_number):
    global digits_list
    print(f"def numbers_count self = {self}, input_number = {input_number}"
          if (debug_mode) else "")
    curr_didgit = self % 10
    self //= 10
    digits_list.append(curr_didgit)
    if self > 0:
        number_reverser(self, input_number)
    else:
        output_str = "".join(map(str, digits_list))
        tm.output_dynamic_string(f"Исходное число {input_number} -> "
                                 f"{output_str}\n")
        return

    #  Main algorithm


input_number = tm.recurse_input_big_int(f"Введите целое натуральное число: ",
                                        NOT_INT_POSITIVE, True, debug_mode)
print(f"Введено число {input_number}" if (debug_mode) else "")
number_reverser(input_number, input_number)
