__author__ = 'Alex Bulavin'
'''
ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
print('Задача 2 дополнительная'.upper())
while not (user_number := input('Введите целое число: ')).isnumeric():
    print("Будьте внимательнее! Введено не число!\n")
digits_sum = 0
for i in user_number:
    digits_sum += int(i)
print(f'Сумма цифр числа {user_number} = {digits_sum}')
