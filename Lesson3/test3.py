__author__ = 'Alex Bulavin'

import os

from library import TypicalMethods as tm
from strings_const import *
from library import bcolors

"""# Очищаем консоль
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
number_reverser(input_number, input_number)"""

"""
task_4

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
      f", их сумма: {sum_calc(start_number, input_number, start_number)}")"""

# task_5
debug_mode = False  # True  #  На время отладки выставляем флаг в True
start_number = 32  # Стартовый код ASCII
end_number = 127  # Конечный код ASCII


def output_ascii(start_num, current_number, end_number):
    if current_number <= end_number:
        # tm.output_dynamic_string(f"{current_number} - "
        #                          f"{chr(current_number)}\t")
        #print(f"{current_number} - {chr(current_number)}\t", end="")
        print('{0:^{1}}'.format(f"{current_number}-{chr(current_number)}",
                                8), end='')
        if (current_number - start_num + 1) % 10 == 0:
            print("\n")
        current_number += 1
        output_ascii(start_num, current_number, end_number)
    else:
        print("\n")
        return


#  Main algorithm
print(bcolors.OKBLUE) 
output_ascii(start_number, start_number, end_number)
print(bcolors.DEFAULT)
