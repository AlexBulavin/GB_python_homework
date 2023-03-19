__author__ = 'Alex Bulavin'
'''
Библиотека типовых методов для их использования в д/з
'''

from strings_const import *  # Импортируем набор текстовых констант
import time
import random
import sys


# Add class for coloring console text
class bcolors:
    """
    Класс для вывода разноцветного текста в консоль
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[55m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREY = '\033[90m'
    BLACK = '\033[90m'
    DEFAULT = '\033[99m'


class TypicalMethods:

    def output_dynamic_string(self):
        """
        Метод имитирует печатную машинку
        Выводит символы со скоростью 1/len(self)
        :return:
        """
        for i in range(len(self)):
            if self is not None:
                time.sleep(1 / len(self))
                sys.stdout.write(self[i])
                sys.stdout.flush()

            if not sys.platform.startswith('darwin'):  # Для Windows
                frequency = random.randint(37, 32767)
                duration = 100  # миллисекунды
                sys.stdout.write('\a')
                sys.stdout.flush()

'''
    // Метод для вывода бегущей строкой 
     /// < summary > Метод для вывода бегущей строкой < / summary >
    // / < param
    name = "text" > Текст который нужно вывести в консоль < / param >
    public static void OutputDynamicString(string text)
    {
        ForegroundColor = ConsoleColor.Blue;
    for (int i = 0; i < text.Length; i++)
    {
        Thread.Sleep(1000 / text.Length);
    Write(text[i]);
    if (!OperatingSystem.IsMacOS()) Beep(Random.Shared.Next(37, 32767), 100);
    }
    ResetColor();
    }'''

    def input_single_int(self):
        """
        Метод ввода целого положительного числа
        На вход получает текст для объяснения пользователю какое число нужно
        ввести.
        Обрабатывает некорректный ввод текста/символов, отрицательных чисел
        :return:
        Возвращает целое положительное число
        """

        flag_input_ok = False
        while not flag_input_ok:
            print(bcolors.OKBLUE)  # Задали цвет текста в консоли
            try:
                if (number_inputs := int(input(
                        f'{TypicalMethods.output_dynamic_string(self)}'
                ))) > 0:
                    flag_input_ok = True
                    return number_inputs
                    print(bcolors.ENDC)  # Возвратили цвет текста к исходному
                else:
                    print(NOT_INT_POSITIVE)
            except ValueError or TypeError:
                print(NOT_INT)
            finally:
                pass

    def input_any_int(self):
        """
        Метод ввода целого числа
        На вход получает текст для объяснения пользователю какое число нужно
        ввести.
        Обрабатывает некорректный ввод текста/символов, отрицательных чисел
        :return:
        Возвращает целое положительное число
        """

        flag_input_ok = False
        while not flag_input_ok:
            print(bcolors.OKBLUE)  # Задали цвет текста в консоли
            try:
                if (number_inputs := input(
                        f'{TypicalMethods.output_dynamic_string(self)}'
                )).isnumeric():
                    flag_input_ok = True
                    return int(number_inputs)
                    print(bcolors.ENDC)  # Возвратили цвет текста к исходному
                else:
                    print(NOT_INT)
            except ValueError or TypeError:
                print(NOT_INT)
            finally:
                pass


class NewException(Exception):
    pass
    # if Exception == 0:
    #     print(f"Вы что? Пытаетесь делить на 0! Введено нулевое "
    #           f"значение, введите знаменатель не равный нолю: ")


# Also add symbol by it ASCII code chr(9610) - marker
'''
age = input(
    f"{bcolors.HEADER}Input your age here {bcolors.ENDC}{chr(9610)}" + ' ')
print(f"{bcolors.OKBLUE}Your age is {bcolors.OKGREEN}{str(age)}")
print(f'Access is permitted: {bcolors.UNDERLINE}{str(int(age) > 18)}')
print(
    f"{bcolors.WARNING}Warning: No active frommets remain. {bcolors.ENDC}Continue?")

print("\033[34m \033[1m \033[3m \033[40m  text")

print('\033[34m\033[1m\033[3m Ready \033[31mfor \033[37msky!')

# # Строки сравниваются посимвольно своими ASCII кодами
# # Функция ord('N') выдаёт ASCII код символа
# print(ord('a'))
# print(ord('b'))
# print('a' > 'b')
# print('hi' > 'hello')
# print(ord('i'), ord('e'))
# print(ord('A'), ord('a'))
#
# x = 10
# y = 23
#
# print(x > y, x < y, x == y)
'''
