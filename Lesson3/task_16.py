__author__ = 'Alex Bulavin'
'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число 
X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов 
в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

'''
from library import TypicalMethods as tm  # Написали вспомогательную либу
# типовых методов и из неё делаем ввод данных

import os
# Очищаем консоль
os.system('clear')

# Просим пользователя ввести количество элементов массива

arr_size = tm.input_single_int(f'Введите количество'
                               f' элементов массива: ')
data_list = []  # Создали пустой список
for i in range(arr_size):  # Заполняем список вводимыми
    # пользователем положительными интами
    data_list.append(tm.input_single_int(f'Введите {i + 1} элемент списка'
                                         f' из {arr_size}: '))
x_counting = tm.input_single_int(f'Введите искомое число: ')

print(f'Число {x_counting} встречается в списке {data_list.count(x_counting)}'
      f' раз')
