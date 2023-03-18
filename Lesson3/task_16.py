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
from library import TypicalMethods

# Просим пользователя ввести количество элементов массива

arr_size = TypicalMethods.input_single_int(f'Введите количество'
                                           f' элементов массива: ')
data_list = []
for i in range(arr_size):
    data_list.append(TypicalMethods.input_single_int(f'Введите '
                                                     f'{i+1} элемент списка'
                                                     f' из {arr_size}: '))
x_counting = TypicalMethods.input_single_int(f'Введите искомое число: ')

print(f'Число {x_counting} встречается в списке {data_list.count(x_counting)}'
      f' раз')


