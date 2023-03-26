__author__ = 'Alex Bulavin'
"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
import os

from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False
odd_count = 0
even_count = 0


def numbers_count(self, input_number):
    self.input_number = input_number
    curr_didgit = self % 10
    if curr_didgit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if self > 9:
        numbers_count(self)
    else:
        tm.output_dynamic_string(f"В числе {input_number} содержится "
                                 f"{even_count} чётных цифр и {odd_count}"
                                 f"нечетных")


#  Main algorithm
input_number = tm.recurse_input_any_int(f"Введите целое натуральное число",
                                        NOT_INT_POSITIVE, True)
numbers_count(input_number)
