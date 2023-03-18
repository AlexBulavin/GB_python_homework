__author__ = 'Alex Bulavin'
'''
## Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 
2k), не превосходящие числа N. 
'''

import math
import time

while not (pow_num := input('Введите целое положительное число '
                            'больше 1: ')).isnumeric():
    print("Введено не число или оно меньше 2, повторите ввод")
pow_num = int(pow_num)
source_num = pow_num
start = time.time()  # точка отсчета времени
pow_num = int(math.log2(pow_num))  # Решаем через логарифм по основанию 2
print(f'Все целые степени двойки (т.е. числа вида 2^k)')
end1 = time.time() - start  # собственно время работы программы
print(f'Время выполнения задачи1 = {end1}')  # вывод времени
for i in range(pow_num + 1):
    print(f'2^{i} = {2 ** i}')

start = time.time()  # точка отсчета времени

i = 0
start = time.time()  # точка отсчета времени
while 2 ** i <= source_num:
    print(2 ** i)
    i += 1
end2 = time.time() - start  # собственно время работы программы
print(f'Время выполнения задачи2 = {end2}')  # вывод времени

print(f"Соотношение времени выполнения = {end2/end1}")
