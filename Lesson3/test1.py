__author__ = 'Alex Bulavin'

from library import TypicalMethods as tm
from library import bcolors

n_elements = tm.input_single_int(f'Введите кол-во '
                                 f'элементов первого множества: ')
m_elements = tm.input_single_int(f'Введите кол-во '
                                 f'элементов второго множества: ')

first_set = set()
tm.set_fill_int(first_set, n_elements, "first_set")

second_set = set()
tm.set_fill_int(second_set, m_elements, "second_set")

print(f'Уникальный набор значений: ', end="")
print(* sorted(list(second_set)))
