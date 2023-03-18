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
<<<<<<< HEAD:task_03.py
    n = n
    nn = n + n
    nnn = nn + n
    result = int(n) + int(nn) + int(nnn)
    print(f'n + n*n + n*n*n = {result}')
=======
    n = int(n)
    nn = n * 10 + n
    nnn = nn * 10 + n
    print(f'n + n*n + n*n*n = {n + nn + nnn}')
>>>>>>> lesson_2:Lesson1/task_03.py
else:
    print(f"Ошибка, ввода!")
