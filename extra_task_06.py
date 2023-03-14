__author__ = 'Alex Bulavin'
'''

Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

# ----------------- РЕШЕНИЕ 1 ---------------------
print('Задача 6 дополнительная. РЕШЕНИЕ 1 частное'.upper())
while not ((ticket_number := input('Введите номер билета (он должен быть '
                                   f'шестизначным числом): ')).isnumeric()
           and (len(ticket_number) == 6)):
    print("Введено не число или оно не шестизначное, повторите ввод\n")

print(f'Ура, билетик счастливый!'
      if (int(ticket_number[0]) +
          int(ticket_number[1]) +
          int(ticket_number[2]) ==
          int(ticket_number[3]) +
          int(ticket_number[4]) +
          int(ticket_number[5]))
      else f'Ничего страшного, не повезло в этот раз')

# ----------------- РЕШЕНИЕ 2 БОЛЕЕ ОБЩЕЕ ---------------------
print('\nЗадача 6 дополнительная. РЕШЕНИЕ 2 БОЛЕЕ ОБЩЕЕ'.upper())
while not ((ticket_number := input('Введите номер билета (он должен быть '
                                   f'чётным числом): ')).isnumeric()
           and (len(ticket_number) % 2 == 0)):
    print("Введено не число или оно нечетное, повторите ввод\n")
first_part = last_part = 0
ticket_number_length = len(ticket_number)
for i in range(ticket_number_length//2):
    first_part += int(ticket_number[i])
    last_part += int(ticket_number[ticket_number_length - i - 1])

print(f'Ура, билетик счастливый!'
      if (first_part == last_part)
      else f'Ничего страшного, не повезло в этот раз')
