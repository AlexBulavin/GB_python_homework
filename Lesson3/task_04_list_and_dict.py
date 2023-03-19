__author__ = 'Alex Bulavin'
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()

"""

from strings_const import *
from library import TypicalMethods as tm
from library import bcolors
from library import NewException
import os

# Очищаем консоль
os.system('clear')


# ---------------- Вариант 1 ------------------
def my_func_1(first_num, second_num, third_num):
    sum_max = 0
    if first_num > second_num > third_num:
        sum_max = first_num + second_num
    elif first_num > second_num <= third_num:
        sum_max = first_num + second_num
    else:
        sum_max = second_num + third_num

    print(f'Сумма наибольших элементов равна {sum_max}')


# ---------------- Вариант 2 ------------------
def my_func_2(**data_num):
    data_num = data_num.sort()

    print(f'Сумма наибольших элементов равна {data_num[0] + data_num[1]}')


print(bcolors.OKBLUE)  # Задали цвет текста в консоли
first_num = tm.input_single_int(f'Введите первое число')
second_num = tm.input_single_int(f'Введите второе число')
third_num = tm.input_single_int(f'Введите третье число')

my_func_1(first_num, second_num, third_num)

my_func_2(first_num, second_num, third_num)

print(bcolors.ENDC)  # Возвратили цвет текста к исходному
