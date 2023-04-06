__author__ = 'Alex Bulavin'
"""Задание 4. Реализовать класс Matrix (матрица). Обеспечить перегрузку 
конструктора класса (метод init()), который должен принимать данные (список 
списков) для формирования матрицы. Подсказка: матрица — система некоторых 
математических величин, расположенных в виде прямоугольной схемы. Примеры 
матриц: 3 на 2, 3 на 3, 2 на 4. 

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в 
привычном виде. Далее реализовать перегрузку метода add() для реализации 
операции сложения двух объектов класса Matrix (двух матриц). Результатом 
сложения должна быть новая матрица. Подсказка: сложение элементов матриц 
выполнять поэлементно — первый элемент первой строки первой матрицы 
складываем с первым элементом первой строки второй матрицы и т.д. """

import os
import inspect

os.environ['TERM'] = 'xterm'
# Очищаем консоль
os.system('clear')

debug_mode = False


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return "\n".join([" ".join(map(str, row))
                          for row in self.list_of_lists])

    def __add__(self, other):
        new_list = []
        if len(self.list_of_lists) != len(other.list_of_lists) or \
                len(self.list_of_lists[0]) != len(other.list_of_lists[0]):
            raise ValueError("Матрицы должны иметь одинаковую размерность")

        for row in range(len(self.list_of_lists)):
            new_raw = []
            for column in range(len(self.list_of_lists[0])):
                if debug_mode:
                    print(f'line {inspect.currentframe().f_lineno} '
                          f'row = {row}, column = {column} \n')
                    print(f'line {inspect.currentframe().f_lineno} '
                          f'{self.list_of_lists}')
                    print(f'line {inspect.currentframe().f_lineno}\n{other}')
                new_item = self.list_of_lists[row][column] + \
                           other.list_of_lists[row][column]
                new_raw.append(new_item)
            new_list.append(new_raw)
        new_maatrix = Matrix(new_list)
        return new_maatrix


list_of_lists1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_lists2 = [[21, 22, 23], [24, 25, 26], [27, 28, 29]]

m1 = Matrix(list_of_lists1)
m2 = Matrix(list_of_lists2)
print(m1)
print('\n')
print(m2)
print('\n')
new_matrix = m1 + m2
print(new_matrix)
