__author__ = 'Alex Bulavin'
'''
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
'''
print('Задание 4'.upper())

print(""
      if (sales := input('Введите выручку фирмы (целое число): ')).isnumeric()
      else "Введено не число", end="")
sales = int(sales)

print(""
      if (loses := input('Введите издержки фирмы (целое число): ')).isnumeric()
      else "Введено не число")
loses = int(loses)

profit = sales - loses
print(f'Финансовый результат - прибыль. Ее величина: {profit}\n'
      f'Значит вычисляем рентабельность выручки '
      f'(соотношение прибыли к выручке)'
      f'\nРентабельность выручки {profit}/{sales} = {round(profit / sales, 1)}'
      if profit > 0 else f'Убыток {profit}')

print(f'Прибыль фирмы в расчете на одного сотрудника = '
      f'{round(profit / int(stuff_num), 1)}'
      if (stuff_num := input(f'Введите количество сотрудников '
                             f'(целое число): ')).isnumeric() and profit > 0
      else "Введено не число")