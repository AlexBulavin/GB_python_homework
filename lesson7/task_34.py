__author__ = 'Alex Bulavin'
'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко 
он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
есть, если число слогов (т.е. число гласных букв) в каждой фразе 
стихотворения одинаковое. Фраза может состоять из одного слова, если во 
фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от 
друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам 
парам”, если с ритмом все не в порядке 

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  

'''
import os
import inspect
import time
import sys
from task_04 import Matrix as m

os.environ['TERM'] = 'xterm'
# Очищаем консоль
os.system('clear')

debug_mode = False


def output_dynamic_string(self):
    for i in range(len(self)):
        print(f'{self[i]}', end="")
        time.sleep(1 / len(self))
        sys.stdout.flush()


print('\033[94m')
output_dynamic_string(f'Ввод:')
silabas = input().lower().split(' ')

# output_dynamic_string(f'{silabas}\n')

glas = 'аеёиоуыэюя'
including_flag = False
including_list = []
glas_counter = 0
item_counter = 0
for frase in silabas:
    for letter in frase:
        for item in glas:
            glas_counter += letter.count(item)
    including_list.append(glas_counter)
    # TODO Сделать сравнение следующего элемента с предыдущим
    including_flag = True if item_counter > 0 \
                             and including_list[item_counter] == \
                             including_list[item_counter - 1] \
        else including_flag
    glas_counter = 0
    item_counter += 1
# output_dynamic_string(f'{including_list} \n')
# print(including_flag)
message = ('Пам парам\n', 'Парам пам-пам\n')[including_flag]
output_dynamic_string(message)
