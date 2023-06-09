__author__ = 'Alex Bulavin'
'''Задание на закрепление знаний по модулю CSV. Написать скрипт, 
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, 
info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого: 
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов 
с данными, их открытие и считывание данных. В этой функции из считанных 
данных необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». 
Значения каждого параметра поместить в соответствующий список. Должно 
получиться четыре списка — например, os_prod_list, os_name_list, 
os_code_list, os_type_list. В этой же функции создать главный список для 
хранения данных отчета — например, main_data — и поместить в него названия 
столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», 
«Код продукта», «Тип системы». Значения для этих столбцов также оформить в 
виде списка и поместить в файл main_data (также для каждого файла); Создать 
функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой 
функции реализовать получение данных через вызов функции get_data(), а также 
сохранение подготовленных данных в соответствующий CSV-файл; Проверить 
работу программы через вызов функции write_to_csv(). 

'''
import csv
import os
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file_name in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        with open(file_name, encoding='1251') as f:
            file_data = f.read()

        os_prod = re.search(r'Изготовитель системы:\s*(.*)', file_data)
        '''Поиск строки в переменной file_data, которая начинается с текста 
        "Изготовитель системы:", за которым следует произвольное количество 
        пробелов (\s*), и затем захватывает любые символы до конца строки с 
        помощью символа (.*). Результат поиска сохраняется в объекте 
        os_prod, который может использоваться для получения значения, 
        соответствующего названию изготовителя системы. 
        Использует модуль re для регулярных выражений, 
        который позволяет осуществлять поиск по шаблону. '''
        os_name = re.search(r'Название ОС:\s*(.*)', file_data)
        os_code = re.search(r'Код продукта:\s*(.*)', file_data)
        os_type = re.search(r'Тип системы:\s*(.*)', file_data)

        if os_prod:
            os_prod_list.append(os_prod.group(1))
            '''Эта строка кода добавляет найденное значение изготовителя 
            операционной системы в список os_prod_list. Метод group(1) 
            объекта os_prod возвращает первую (и единственную) группу 
            захвата в регулярном выражении, которая содержит захваченные 
            символы, соответствующие шаблону поиска в скобках (.*). Это 
            значит, что os_prod.group(1) содержит значение, соответствующее 
            названию изготовителя операционной системы, найденного с помощью 
            регулярного выражения в предыдущей строке кода. Затем, найденное 
            значение добавляется в конец списка os_prod_list с помощью 
            метода append(), чтобы можно было использовать это значение 
            позже в программе. '''
        if os_name:
            os_name_list.append(os_name.group(1))
        if os_code:
            os_code_list.append(os_code.group(1))
        if os_type:
            os_type_list.append(os_type.group(1))

        main_data.append([os_prod.group(1), os_name.group(1), os_code.group(1),
                          os_type.group(1)])

    return main_data


def write_to_csv(csv_file):
    main_data = get_data()

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(main_data)


csv_file = 'report.csv'
write_to_csv(csv_file)
