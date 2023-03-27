__author__ = 'Alex Bulavin'
"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

import os

from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

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

