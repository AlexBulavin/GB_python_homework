__author__ = 'Alex Bulavin'
'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между 
дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no

'''
print('\nЗадача 8 дополнительная'.upper())
while not (chocolate_length := input(
        'Введите ширину шоколадки в дольках'
        f'(она должна быть натуральным числом): ')).isnumeric() \
        and (int(chocolate_length) > 0):
    "Введено не число или оно меньше или равно нолю, повторите ввод"
while not (chocolate_width := input(
        'Введите длину шоколадки в дольках '
        f'(она должна быть натуральным числом): ')).isnumeric() \
        and (int(chocolate_width) > 0):
    "Введено не число или оно меньше или равно нолю, повторите ввод"
pieces_amount = input(f'Шоколадка {chocolate_length}X'
                      f'{chocolate_width}'
                      f'На какое количество будем делить?')
chocolate_length = int(chocolate_length)
chocolate_width = int(chocolate_width)
if (pieces_amount.isnumeric()
        and (int(pieces_amount) > 0)
        and (int(pieces_amount) >= chocolate_length
             or int(pieces_amount) >= chocolate_width)
        and (int(pieces_amount) % chocolate_length == 0
             or int(pieces_amount) % chocolate_width == 0)
        and (int(pieces_amount) <= (chocolate_width * chocolate_length -
                                    min(chocolate_width, chocolate_length)))):
    print(f'Шоколадка делится на {pieces_amount}!')
else:
    print(f'Не делится.')

