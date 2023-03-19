__author__ = 'Alex Bulavin'
"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

from strings_const import *
from library import TypicalMethods as tm
from library import bcolors
from library import NewException
import os

# Очищаем консоль
os.system('clear')


def print_user_data(**kwargs):
    print(f'{user_first_name} '
          f'{user_last_name} '
          f'{user_birth_year} года рождения, '
          f'проживает в городе {user_living_city},'
          f' email: {user_email}'
          f', телефон: {user_phone1}')


print(bcolors.OKBLUE)  # Задали цвет текста в консоли
user_first_name = input(tm.output_dynamic_string(USER_FIRST_NAME_REQUEST))
user_last_name = input(tm.output_dynamic_string(USER_LAST_NAME_REQUEST))
user_birth_year = tm.input_single_int(USER_BIRTH_YEAR_REQUEST)
user_living_city = input(tm.output_dynamic_string(USER_LIVING_CITY))
user_email = input(tm.output_dynamic_string(USER_EMAIL))
user_phone1 = input(tm.output_dynamic_string(USER_PHONE1))

print_user_data(user_first_name=user_first_name,
                user_last_name=user_last_name,
                user_birth_year=user_birth_year,
                user_living_city=user_living_city,
                user_email=user_email,
                user_phone1=user_phone1
                )
print(bcolors.ENDC)  # Возвратили цвет текста к исходному
