__author__ = 'Alex Bulavin'
'''
## Задача 12:
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''
import math

print('Задание 12'.upper())
while not (x_plus_y := input('Введите сумму Х + Y: ')).isnumeric():
    print("Введено не число, повторите ввод")
x_plus_y = int(x_plus_y)
print(f'x_plus_y = {x_plus_y}')
while not (x_multiply_y := input('Введите произведение Х * Y: ')).isnumeric():
    print("Введено не число, повторите ввод")
x_multiply_y = int(x_multiply_y)
print(f'x_multiply_y = {x_multiply_y}')

discriminant = x_plus_y ** 2 - 4 * x_multiply_y
print(f'discriminant = {discriminant}')

if discriminant > 0:
    y1 = (x_plus_y + math.sqrt(discriminant)) / 2
    if y1 != 0:
        x1 = x_plus_y - y1
        print(f"Первая пара значений X1 = {int(x1)}, Y1 = {int(y1)}")
    else:
        print("Первый корень уравнения = 0")

    y2 = (x_plus_y - math.sqrt(discriminant)) / 2
    if y2 != 0:
        x2 = x_plus_y - y2
        print(f"Вторая пара значений X2 = {int(x2)}, Y1 = {int(y2)}")
    else:
        print("Второй корень уравнения равен 0")

else:
    print(f"Дискриминант отрицательный, корень управления комплексный!")
