__author__ = 'Alex Bulavin'
"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
from strings_const import *
from library import TypicalMethods as tm
from library import bcolors
from library import NewException
import os

# Очищаем консоль
os.system('clear')
second_num = 0
first_num = tm.input_any_int(f"Введите числитель: ")
while not second_num:
    try:
        second_num = tm.input_any_int(f"Введите знаменатель не равный нолю: ")
        if second_num == 0:
            raise NewException()
        else:
            print(f'{first_num} / {second_num} = '
                  f'{(first_num / second_num) :.2f}')

    except NewException:
        print(f"{bcolors.RED}Вы что? Пытаетесь делить на 0!\n"
              f"Введено нулевое значение, введите"
              f" знаменатель не равный нолю: {bcolors.ENDC}")
