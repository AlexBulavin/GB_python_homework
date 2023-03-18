__author__ = 'Alex Bulavin'

'''
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
'''

print('Задание 3'.upper())

n = input('Введите целое положительное число n: ')
if n.isnumeric() and (int(n) > 0):
    n = n
    nn = int(n)*2
    nnn = int(n)*3
    print(f'n + n*n + n*n*n = {n + str(nn) + str(nnn)}')
else:
    print(f"Ошибка, ввода!")
