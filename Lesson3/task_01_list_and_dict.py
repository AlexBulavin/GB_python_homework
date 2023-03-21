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
    month_number = tm.input_single_int(f"Введите номер месяца: ")
    month_number = month_number % 12 # Обработка чисел больше 12
    if 1 <= month_number:
        match month_number:
            case 1:
                print(SEASONS_LIST[0])
            case 2:
                print(SEASONS_LIST[0])
            case 12:
                print(SEASONS_LIST[0])
            case 3:
                print(SEASONS_LIST[1])
            case 4:
                print(SEASONS_LIST[1])
            case 5:
                print(SEASONS_LIST[1])
            case 6:
                print(SEASONS_LIST[2])
            case 7:
                print(SEASONS_LIST[2])
            case 8:
                print(SEASONS_LIST[2])
            case 9:
                print(SEASONS_LIST[3])
            case 10:
                print(SEASONS_LIST[3])
            case 11:
                print(SEASONS_LIST[3])

seasons_list()


def seasons_dict():
    print(SEASONS_DICT[tm.input_single_int(f"Введите номер месяца: ") % 12]) # % 12 = Обработка чисел больше 12


seasons_dict()
