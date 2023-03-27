__author__ = 'Alex Bulavin'

import os

from library import TypicalMethods as tm
from strings_const import *
from library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # True

"""def sum_natural(self):
    if self == 1:
        return 1
    return self + sum_natural(self - 1)


# Проверяем для произвольного user_input
user_input = tm.recurse_input_natural(f"Введите произвольное число: ",
                                      NOT_INT_POSITIVE_OR_TEXT, debug_mode)
left_sum = sum_natural(user_input)
right_sum = user_input * (user_input + 1) / 2

if left_sum == right_sum:
    print(f"Сумма по формуле 1+2+...+n для n={user_input} == n * (n + 1) / 2 ="
          f" {left_sum}")
else:
    print(f"Сумма по формуле 1+2+...+n для n={user_input} - n * (n + 1) / 2 = "
          f"{left_sum - right_sum} ")
    """


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
