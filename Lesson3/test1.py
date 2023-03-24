__author__ = 'Alex Bulavin'

from library import TypicalMethods as tm
from timeit import timeit
import os

# Очищаем консоль
os.system('clear')

debug_mode = False

bush_amount = 0
# TODO: Рандомайзер заполнения
# Делаем запрос количества кустов на грядке. Минимум 3 максимум 12
# запрашиваем у пользователя
while 3 > bush_amount or bush_amount > 12:
    bush_amount = tm.input_single_int(f'Введите число кустов на грядке от 3 до'
                                      f' 12: ')
    if 3 > bush_amount > 12:
        tm.output_dynamic_string(
            f'Введённое число кустов на грядке меньше 3 или'
            f'больше 12. Повторите ввод.')

# TODO: Делаем во внешней библиотеке модуль рандомного заполнения списка
# и заполняем список
# self, n_elements, min_int, max_int,
# min_included, min_included, self_name, debug_mode
ridge_list = []
tm.list_fill_random_int(ridge_list, bush_amount, 3, 12, True, True,
                        "ridge_list", debug_mode)
bush_amount -= 1
sum_berries_max = 0
sum_berries_tripple = 0
alt_sum_berries_tripple = 0
alt_sum_berries_max = 0
max_index = 0
alt_max_index = 0
repeats = 100000
alt_time = 0
main_time = 0
# Кольцевой список - основная логика. Проход по всем тройкам.

for i in range(bush_amount):
    main_time = timeit("""
if debug_mode: print(f"Main algorithm ")
sum_berries_tripple += ridge_list[i]
if i < bush_amount - 1:
    sum_berries_tripple += ridge_list[i + 1]
    sum_berries_tripple += ridge_list[i + 2]
    if debug_mode: print(
        f'sum_berries_tripple {i} = {sum_berries_tripple}')
if i == bush_amount - 1:
    sum_berries_tripple += ridge_list[i + 1]
    sum_berries_tripple += ridge_list[0]
    if debug_mode: print(
        f'sum_berries_tripple {i} = {sum_berries_tripple}')
if i == bush_amount:
    sum_berries_tripple += ridge_list[0]
    sum_berries_tripple += ridge_list[1]
    if debug_mode: print(
        f'sum_berries_tripple {i} = {sum_berries_tripple}')
if sum_berries_tripple > sum_berries_max:
    sum_berries_max = sum_berries_tripple
    max_index = i

""", setup="from __main__ import ridge_list, bush_amount, "
           "sum_berries_tripple, sum_berries_max, i, "
           "max_index, debug_mode", number=repeats)

    # ---------------- Альтернативный алгоритм из эталонного решения
    alt_time = timeit("""
if debug_mode: print(f"Alt algorithm 1")
alt_sum_berries_tripple = ridge_list[i - 1] + ridge_list[i] + ridge_list[
    i + 1]
if alt_sum_berries_tripple > alt_sum_berries_max:
    alt_sum_berries_max = alt_sum_berries_tripple
    alt_max_index = i
    """, setup="from __main__ import ridge_list, bush_amount, "
               "sum_berries_tripple, sum_berries_max, i, max_index, "
               "debug_mode, alt_sum_berries_tripple, alt_sum_berries_max, "
               "alt_max_index", number=repeats)
alt_time += timeit("""
if debug_mode: print(f"Alt algorithm 2")
alt_sum_berries_max = ridge_list[-2] + ridge_list[-1] + ridge_list[0]
if alt_sum_berries_tripple > alt_sum_berries_max:
   alt_sum_berries_max = alt_sum_berries_tripple
   alt_max_index = len(ridge_list) - 1
""", setup="from __main__ import ridge_list, bush_amount, "
           "sum_berries_tripple, sum_berries_max, i, "
           "max_index, debug_mode, alt_sum_berries_tripple, "
           "alt_sum_berries_max, alt_max_index", number=repeats)

# Иллюстрация решения
print(*ridge_list)
print(f'Максимальная троица от {max_index + 1} куста: {sum_berries_max}')
print(main_time)
print(f'Alt Максимальная троица от {max_index + 1} куста: {sum_berries_max}')
print(alt_time)
