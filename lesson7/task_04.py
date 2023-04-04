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

    def __str__(self, message):
        print(f'{message}')
        for row in message:
            for column in row:
                print(column, end='\t')
            print(f'\n')

    def add(self, other):
        new_list = []

        for row in range(len(self.list_of_lists)):
            new_raw = []
            for column in range(len(self.list_of_lists[0])):
                if debug_mode:
                    print(f'line {inspect.currentframe().f_lineno} row = {row}, '
                          f'column = {column} \n')
                    print(self.list_of_lists)
                    print(other)
                    print(self.list_of_lists[row][column] + \
                          other[row][column])
                new_raw.append(self.list_of_lists[row][column] + \
                                       other[row][column])
            new_list.append(new_raw)
        return Matrix(new_list)


list_of_lists1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_lists2 = [[21, 22, 23], [24, 25, 26], [27, 28, 29]]

m1 = Matrix(list_of_lists1)
m2 = Matrix(list_of_lists2)
m3 = Matrix(list_of_lists1)

matrix1 = m1.__str__(f'Задана матрица 1:')
matrix2 = m2.__str__(f'Задана матрица 2:')

new_matrix = m3.add(list_of_lists2).__str__(f'Сумма матриц:')
