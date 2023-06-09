__author__ = 'Alex Bulavin'
# 
# from library import TypicalMethods as tm
# from strings_const import *
# from library import bcolors
# 
# import os
# 
# # Очищаем консоль
# os.system('clear')
# 
# debug_mode = False
# 
# print(f"Test", debug_mode)
# 
# number1 = number2 = 0
# user_operation_input = ""
# user_input = ""
# 
# def not_null_input():
#     number2 = tm.input_any_int(f"Введите второе число: ")
#     if number2 == 0:
#         print(f"На ноль делить нельзя!!!")
#         not_null_input()
#     return number2
# 
# 
# def input_operation():
#     tm.output_dynamic_string(f"Введите операцию (+, -, *, / или "
#                              f"0 для выхода):")
#     user_input = input()
#     operation_list = ["+", "-", "*", "/", "0"]
#     if user_input not in operation_list:
#         tm.output_dynamic_string(f"Вы вместо трехзначного числа "
#                                  f"ввели строку (((. Исправьтесь")
#         print()
#         if debug_mode:
#             print(f"user_input = {user_input}")
#         user_input = input_operation()
# 
#     if debug_mode:
#         print(f"43 user_input = {user_input}")
#     return user_input
# 
# 
# def print_result(number1=number1, number2=number2,
#                  user_operation_input=user_operation_input):
#     number1 = int(number1)
#     number2 = int(number2)
#     user_operation_input = str(user_operation_input)
#     if user_operation_input == "+":
#         if debug_mode:
#             print(f"number1 - {type(number1)}, number2 - {type(number2)},"
#                   f"user_operation_input - {type(user_operation_input)}")
#         print(f"{number1} {user_operation_input} {number2} = "
#               f"{number1 + number2}")
#     elif user_operation_input == "-":
#         if debug_mode:
#             print(f"number1 - {type(number1)}, number2 - {type(number2)},"
#                   f"user_operation_input - {type(user_operation_input)}")
#         print(f"{number1} {user_operation_input} {number2} = "
#               f"{number1 - number2}")
#     elif user_operation_input == "*":
#         if debug_mode:
#             print(f"number1 - {type(number1)}, number2 - {type(number2)},"
#                   f"user_operation_input - {type(user_operation_input)}")
#         print(f"{number1} {user_operation_input} {number2} = "
#               f"{number1 * number2}")
#     else:
#         if debug_mode:
#             print(f"number1 - {type(number1)}, number2 - {type(number2)},"
#                   f"user_operation_input - {type(user_operation_input)}")
#         print(f"{number1} {user_operation_input} {number2} = "
#               f"{number1 / number2}")
# 
# 
# def main_code():
#     number1 = tm.recurse_input_any_int(f"Введите первое число: ", WRONG_INPUT)
#     number2 = tm.recurse_input_any_int(f"Введите второе число: ", WRONG_INPUT)
#     user_operation_input = input_operation()
#     if user_operation_input == "0":
#         print(bcolors.CYAN)  # Задали цвет текста в консоли
#         tm.output_dynamic_string(SEE_YOU_SOON)
#         print(bcolors.ENDC)  # Возвратили цвет текста к исходному
#         return
#     elif user_operation_input == "/" and number2 == 0:
#         print(bcolors.RED)  # Задали цвет текста в консоли
#         tm.output_dynamic_string(f"На {number2} делить нельзя.")
#         print(bcolors.OKBLUE)  # Задали цвет текста в консоли
#         number2 = not_null_input()
#     print_result(number1, number2, user_operation_input)
#     main_code()
# 
# 
# main_code()

import os

from library import TypicalMethods as tm
from strings_const import *
from library import bcolors

# Очищаем консоль
os.system('clear')

debug_mode = False  # На время отладки выставляем флаг в True
odd_count = 0
even_count = 0


def numbers_count(self, input_number):
    global odd_count, even_count, debug_mode
    print(f"def numbers_count self = {self}, input_number = {input_number}" 
          if (debug_mode) else "")
    curr_didgit = self % 10
    self //= 10
    
    print(f"def numbers_count curr_didgit = {curr_didgit} self = {self}"
          if (debug_mode) else "")
    if curr_didgit % 2 == 0:
        even_count += 1
        print(f"def numbers_count even_count = {even_count}"
              if (debug_mode) else "")
    else:
        odd_count += 1
        print(f"def numbers_count odd_count = {odd_count}"
              if (debug_mode) else "")
    if self > 0:
        numbers_count(self, input_number)
    else:
        tm.output_dynamic_string(f"В числе {input_number} содержится "
                                 f"{even_count} чётных цифр и {odd_count}"
                                 f" нечетных\n")
        return 


#  Main algorithm
input_number = tm.recurse_input_big_int(f"Введите целое натуральное число: ",
                                        NOT_INT_POSITIVE, True)
print(f"Введено число {input_number}" if (debug_mode) else "", end="")
numbers_count(input_number, input_number)

