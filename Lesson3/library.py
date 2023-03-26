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
            if self[i] is not None:
                sys.stdout.write(self[i])
                sys.stdout.flush()
                time.sleep(1 / (1.5 * len(self)))
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

    def output_dynamic_string_v2(self):
        for i in range(len(self)):
            print(f'{self[i]}', end="")
            time.sleep(1 / len(self))
            sys.stdout.flush()

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
                TypicalMethods.output_dynamic_string(self)
                if (number_inputs := int(input())) > 0:
                    flag_input_ok = True
                    print(bcolors.ENDC)  # Возвратили цвет текста к исходному
                    return number_inputs
                else:
                    print(NOT_INT_POSITIVE)
            except ValueError or TypeError:
                print(NOT_INT)
            finally:
                pass

    def input_any_int(self, message=NOT_INT) -> int:
        """
        Метод ввода целого числа
        На вход получает текст для объяснения пользователю какое число нужно
        ввести.
        И опционально сообщение на случай некорректного ввода
        Обрабатывает некорректный ввод текста/символов, отрицательных чисел
        :return:
        Возвращает целое положительное число
        """
        flag_input_ok = False
        while not flag_input_ok:
            print(bcolors.OKBLUE)  # Задали цвет текста в консоли
            try:
                TypicalMethods.output_dynamic_string(self)
                if (number_inputs := input()).isnumeric():
                    flag_input_ok = True
                    return int(number_inputs)
                else:
                    print(message)
            except ValueError or TypeError:
                print(message)
            finally:
                pass
        print(bcolors.ENDC)  # Возвратили цвет текста к исходному

    def set_fill_int(self, n_elements, self_name):
        """
        Заполняет структуру на входе в параметре self интами
        :param n_elements: количество элементов структуры self,
        например, множества
        :return: возвращает структуру, заполненную интами из инпута
        """
        for i in range(n_elements):
            self.add(TypicalMethods.input_any_int(f'Введите {i + 1} '
                                                  f'элемент из {n_elements} для'
                                                  f' {self_name} множества: '))
        return self

    def list_fill_random_int(self, n_elements, min_int, max_int, min_included,
                             max_included, self_name, debug_mode):
        # self, n_elements, min_int, max_int,
        # min_included, min_included, self_name, debug_mode
        """
        Заполняет структуру на входе в параметре self случайными интами в
        диапазоне min_int - max_int
        включая/исключая их (min_included/max_included = True/False)
        :param n_elements: количество элементов структуры self,
        например, множества, список
        :return: возвращает структуру, заполненную случайными интами
        """
        # Ниже приведен генератор списка. Проблема в том, что он выдаёт пустой
        # список, если условие не выполняется
        # self = [random.randint(min_int, max_int) for i in range(n_elements) if
        #         min_included and max_included]
        # self = [random.randint(min_int, max_int - 1) for i in range(n_elements)
        #         if min_int and not max_included and max_included -
        #         min_included > 1]
        # self = [random.randint(min_int + 1, max_int - 1) for i in
        #         range(n_elements) if not min_int and not max_included and
        #         max_included - min_included > 2]
        # 
        for i in range(n_elements):
            if min_included and max_included:
                self.append(random.randint(min_int, max_int))

            elif min_int and not max_included and max_included - \
                    min_included > 1:
                self.append(random.randint(min_int, max_int - 1))
            elif not min_int and not max_included and max_included - \
                    min_included > 2:
                self.append(random.randint(min_int + 1, max_int - 1))
            else:
                if debug_mode:
                    print(f'Введённые параметры min и '
                          f'max для {self_name} должны отличаться больше')
        return self

    def recurse_input_any_int(self, message=NOT_INT, is_positive=False) -> int:
        """
        Метод ввода целого числа рекурсионной проверкой
        На вход получает текст для объяснения пользователю какое число нужно
        ввести.
        И опционально сообщение на случай некорректного ввода
        Обрабатывает некорректный ввод текста/символов, отрицательных чисел
        :return:
        Возвращает целое положительное число
        """
        print(bcolors.OKBLUE)  # Задали цвет текста в консоли
        try:
            TypicalMethods.output_dynamic_string(self)
            if (number_inputs := input()).isnumeric() and is_positive:
                print(bcolors.ENDC)
                return int(number_inputs)
            else:
                print(message)
                return TypicalMethods.recurse_input_any_int(self, message)
        except ValueError or TypeError:
            print(message)
            return TypicalMethods.recurse_input_any_int(self, message)
        finally:
            print(bcolors.ENDC)  # Возвратили цвет текста к исходному

    def recurse_input_big_int(self, message=NOT_INT, is_positive=False, 
                              debug_mode=False) -> int:
        """
        Метод ввода целого числа рекурсионной проверкой
        На вход получает текст для объяснения пользователю какое число нужно
        ввести.
        И опционально сообщение на случай некорректного ввода
        Обрабатывает некорректный ввод текста/символов, отрицательных чисел
        :return:
        Возвращает целое положительное число
        """
        print(bcolors.OKBLUE)  # Задали цвет текста в консоли
        try:
            TypicalMethods.output_dynamic_string(self)
            if (number_inputs := input()).isnumeric() and is_positive:
                print(f"number_inputs from recurse_input_big_int = "
                      f"{number_inputs}" if (debug_mode) else "", end="")
                print(bcolors.ENDC)
                return int(number_inputs)
            else:
                print(message)
                return TypicalMethods.recurse_input_any_int(self, message)
        except ValueError or TypeError:
            print(message)
            return TypicalMethods.recurse_input_any_int(self, message)
        finally:
            print(bcolors.ENDC)  # Возвратили цвет текста к исходному


'''
while True:
    try:
        a = int(input("Введите число A: "))
        b = int(input("Введите число B: "))
    except ValueError:
        print("Введите целое натуральное число!")
    else:
        if b < 0:
            print("B не может быть меньше 0")
        else:
            break
print(my_pow(a, b))
'''


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
