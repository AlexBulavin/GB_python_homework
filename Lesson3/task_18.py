__author__ = 'Alex Bulavin'
'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
 числу X. Пользователь в первой строке вводит натуральное число N – количество 
 элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
 Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

from library import TypicalMethods as tm  # Написали вспомогательную либу
# типовых методов и из неё делаем ввод данных

import os

# Очищаем консоль
os.system('clear')

# Просим пользователя ввести количество элементов массива

arr_size = tm.input_single_int(f'Введите количество'
                               f' элементов массива: ')

x_diff = tm.input_single_int(f'Введите число, которое сравниваем: ')

data_list = []  # Создали пустой список
for i in range(arr_size):  # Заполняем список вводимыми
    # пользователем положительными интами
    data_list.append(tm.input_single_int(f'Введите {i + 1} элемент списка'
                                         f' из {arr_size}: '))
    if i == 0:
        old_diff = abs(data_list[i] - x_diff)
        current_diff = old_diff
        min_diff_item = data_list[i]
    else:
        current_diff = abs(data_list[i] - x_diff)
        if current_diff < old_diff:
            old_diff = current_diff
            min_diff_item = data_list[i]

print(f"Минимально отличающееся от {x_diff} число = {min_diff_item}")
