__author__ = 'Alex Bulavin'
'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с 
повторениями). Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

from ..lesson3.library import TypicalMethods as tm
from library import bcolors
from library import NewException
from ..lesson3.strings_const import *
import os

# Очищаем консоль
os.system('clear')

n_elements = tm.input_single_int(f'Введите кол-во '
                                 f'элементов первого множества: ')
m_elements = tm.input_single_int(f'Введите кол-во '
                                 f'элементов второго множества: ')

first_set = set()
tm.set_fill_int(first_set, n_elements, "first_set")

second_set = set()
tm.set_fill_int(second_set, m_elements, "second_set")

print(f'Уникальный набор значений: ', end="")
print(* sorted(list(second_set)))
