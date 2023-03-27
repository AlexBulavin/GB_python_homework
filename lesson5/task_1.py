__author__ = 'Alex Bulavin'
"""
git remote add origin
Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
from ..lesson3.library import TypicalMethods as tm
from ..lesson3.strings_const import *
from ..lesson3.library import bcolors

import os

# Очищаем консоль
os.system('clear')

debug_mode = False

print(f"Test", debug_mode)

number1 = number2 = 0
user_operation_input = ""
user_input = ""


def not_null_input():
    number2 = tm.input_any_int(f"Введите второе число: ")
    if number2 == 0:
        print(f"На ноль делить нельзя!!!")
        not_null_input()
    return number2


def input_operation():
    tm.output_dynamic_string(f"Введите операцию (+, -, *, / или "
                             f"0 для выхода):")
    user_input = input()
    operation_list = ["+", "-", "*", "/", "0"]
    if user_input not in operation_list:
        tm.output_dynamic_string(f"Вы вместо трехзначного числа "
                                 f"ввели строку (((. Исправьтесь")
        print()
        if debug_mode:
            print(f"user_input = {user_input}")
        user_input = input_operation()

    if debug_mode:
        print(f"43 user_input = {user_input}")
    return user_input


def print_result(number1=number1, number2=number2,
                 user_operation_input=user_operation_input):
    number1 = int(number1)
    number2 = int(number2)
    user_operation_input = str(user_operation_input)
    if user_operation_input == "+":
        if debug_mode:
            print(f"number1 - {type(number1)}, number2 - {type(number2)},"
                  f"user_operation_input - {type(user_operation_input)}")
        print(f"{number1} {user_operation_input} {number2} = "
              f"{number1 + number2}")
    elif user_operation_input == "-":
        if debug_mode:
            print(f"number1 - {type(number1)}, number2 - {type(number2)},"
                  f"user_operation_input - {type(user_operation_input)}")
        print(f"{number1} {user_operation_input} {number2} = "
              f"{number1 - number2}")
    elif user_operation_input == "*":
        if debug_mode:
            print(f"number1 - {type(number1)}, number2 - {type(number2)},"
                  f"user_operation_input - {type(user_operation_input)}")
        print(f"{number1} {user_operation_input} {number2} = "
              f"{number1 * number2}")
    else:
        if debug_mode:
            print(f"number1 - {type(number1)}, number2 - {type(number2)},"
                  f"user_operation_input - {type(user_operation_input)}")
        print(f"{number1} {user_operation_input} {number2} = "
              f"{number1 / number2}")


def main_code():
    user_operation_input = input_operation()
    if user_operation_input == "0":
        print(bcolors.CYAN)  # Задали цвет текста в консоли
        tm.output_dynamic_string(SEE_YOU_SOON)
        print(bcolors.ENDC)  # Возвратили цвет текста к исходному
        return
    number1 = tm.recurse_input_any_int(f"Введите первое число: ", WRONG_INPUT)
    number2 = tm.recurse_input_any_int(f"Введите второе число: ", WRONG_INPUT)
    if user_operation_input == "/" and number2 == 0:
        print(bcolors.RED)  # Задали цвет текста в консоли
        tm.output_dynamic_string(f"На {number2} делить нельзя.")
        print(bcolors.OKBLUE)  # Задали цвет текста в консоли
        number2 = not_null_input()
    print_result(number1, number2, user_operation_input)
    main_code()


main_code()
