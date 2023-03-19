__author__ = 'Alex Bulavin'
'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
'''
from strings_const import *
from library import TypicalMethods as tm
from library import bcolors
import os

# Очищаем консоль
os.system('clear')


def seasons_list():
    month_number = tm.input_single_int(f'{bcolors.OKBLUE}'
           f'{TypicalMethods.input_single_int(f"Введите номер месяц:")}'
           f'{bcolors.ENDC}')

    match month_number:
        case 1, 2, 12:
            print(SEASONS_LIST[0])
        case 3, 4, 5:
            print(SEASONS_LIST[1])
        case 6, 7, 8:
            print(SEASONS_LIST[2])
        case 9, 10, 11:
            print(SEASONS_LIST[3])


seasons_list()
