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

"""
def sum_a_b(a, b):
    if b == 0:
        return a
    else:
        return sum_a_b(a + 1, b - 1)

print('\033[92m', 'Ptktysq ntrcn')
print(bcolors.DEFAULT)
input_a = tm.recurse_input_natural(f"Введите первое слагаемое: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
input_b = tm.recurse_input_natural("Введите второе слагаемое: ",
                                   NOT_INT_POSITIVE_OR_TEXT, debug_mode)
tm.output_dynamic_string(f'{input_a}+{input_b} = '
                         f'{sum_a_b(input_a, input_b)}\n')"""

"""def an_element(a1, n, d, counter):
    print(f"a{counter} = {a1 + (counter - 1) * d:.2f}")
    counter += 1
    if counter <= n:
        return an_element(a1, n, d, counter)
    return


input_a1 = tm.input_any_float(f"Введите чтсло - первый элемент прогрессии: ",
                              NOT_INT_POSITIVE_OR_TEXT, debug_mode)

input_d = tm.input_any_float("Введите число - разность прогрессии: ",
                           NOT_INT_POSITIVE_OR_TEXT, debug_mode)

input_n = tm.input_any_int("Введите натуральное число - "
                           "количество элементов прогрессии: ",
                           NOT_INT_POSITIVE_OR_TEXT, debug_mode)

an_element(input_a1, input_n, input_d, 1)
"""
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
