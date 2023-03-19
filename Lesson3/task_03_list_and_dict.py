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


def user_data(**kwargs):
    print(f'{user_first_name} '
          f'{user_last_name} '
          f'{user_birth_yaer} года рождения'
          f'проживает в городе {user_living_city}'
          f' email: {user_email}'
          f', телефон: {user_phone1}')


user_first_name = input(USER_FIRST_NAME_REQUEST)
user_last_name = input(USER_LAST_NAME_REQUEST)
user_birth_year = tm.input_single_int(USER_BIRTH_YEAR_REQUEST)
user_living_city = input(USER_LIVING_CITY)
user_email = input(USER_EMAIL)
user_phone1 = input(USER_PHONE1)


