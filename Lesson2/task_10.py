__author__ = 'Alex Bulavin'
'''
## Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

while not ((coins_num := input('Введите количество монет -целое положительное '
                               'число больше 1: ')).isnumeric()
           and int(coins_num) >= 1):
    print("Введено не число или оно меньше 1, повторите ввод\n")
coins_num = int(coins_num)
zero_coins = eagle_coins = 0

for i in range(coins_num):
    while not ((coin := input(
            f'Введите значение монетки {i+1} из {coins_num}. 1 - орёл, 0 - '
            f'решка: ')).isnumeric() and 0 <= int(coin) <= 1):
        print("Введено не число или оно не в диапазоне 0..1, повторите ввод\n")
    coin = int(coin)
    if coin == 0:
        zero_coins += 1
    else:
        eagle_coins += 1
    print(f'Решки = {zero_coins}, Гербы = {eagle_coins}')

print(f'Из {coins_num} монет ', end='')

if zero_coins < eagle_coins:
    print(f'{zero_coins} решкой вверх, нужно перевернуть')
elif zero_coins == eagle_coins:
    print(f'можно перевернуть любые монетки, количество гербов и решек '
          f'одинаковое = {zero_coins}')
else:
    print(f'{eagle_coins} гербом вверх, нужно перевернуть')
