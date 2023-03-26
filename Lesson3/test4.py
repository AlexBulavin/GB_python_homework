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


def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a * a, b / 2)
    else:
        return a * power(a * a, (b - 1) / 2)


input_a = tm.recurse_input_natural(f"Введите значение основания степени: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
input_b = tm.recurse_input_natural("Введите значение показателя степени: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
tm.output_dynamic_string(f'{input_a}^{input_b} = {power(input_a, input_b)}\n')
