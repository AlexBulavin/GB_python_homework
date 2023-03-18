__author__ = 'Alex Bulavin'
'''
Библиотека типовых методов для их использования в д/з
'''


class TypicalMethods:
    # Делаем набор текстовых констант
    global not_int_positive
    not_int_positive = "Введено отрицательное число, повторите ввод"
    global not_int
    not_int = "Введено не целое число, повторите ввод"

    def input_single_int(self):
        flag_input_ok = False
        while not flag_input_ok:
            try:
                if (number_inputs := int(input(self))) > 0:
                    flag_input_ok = True
                    return number_inputs
                else:
                    print(not_int_positive)
            except ValueError or TypeError:
                print(not_int)
            finally:
                pass

