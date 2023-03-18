__author__ = 'Alex Bulavin'
'''
Библиотека типовых методов для их использования в д/з
'''

from strings_const import *  # Импортируем набор текстовых констант



# Add class for coloring console text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[55m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class TypicalMethods:

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
            try:
                if (number_inputs := int(input(f'{bcolors.OKBLUE}{self}'
                                               f'{bcolors.ENDC}'))) > 0:
                    flag_input_ok = True
                    return number_inputs
                else:
                    print(NOT_INT_POSITIVE)
            except ValueError or TypeError:
                print(NOT_INT)
            finally:
                pass


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
