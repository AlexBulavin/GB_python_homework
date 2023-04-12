__author__ = 'Alex Bulavin'
'''
1) реализовать дескрипторы для любых двух классов
'''


class NameType:
    # def __init__(self, incoming_attr):
    #     self.incoming_attr = incoming_attr

    def __get__(self, instance, owner):  # Здесь
        # self - экземпляр класса PositiveNumber
        # instance - это экземпляр вызывающего класса, например, Person
        # owner - сам вызывающий класс, например, ivan
        return instance.__dict__[self.incoming_attr]  # Все атрибуты объекта
        # хранятся в словаре
        # Здесь мы не изменили поведение __get__, на выход метода отдали
        # входящее значение return instance.__dict__[self.incoming_attr]

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Тип данных должен быть str")
        num_in_name = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        intersection = num_in_name.intersection(set(value))
        print('intersection = ', intersection)
        if len(intersection):
            raise ValueError("Цифры не могут использоваться в имени")
        instance.__dict__[self.incoming_attr] = value  # Можно не писать эту
        # строку

    def __delete__(self, instance):
        del instance.__dict__[self.incoming_attr]

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr


class PositiveNumber:
    # def __init__(self, incoming_attr):
    #     self.incoming_attr = incoming_attr

    def __get__(self, instance, owner):  # Здесь
        # self - экземпляр класса PositiveNumber
        # instance - это экземпляр вызывающего класса, например, Person
        # owner - сам вызывающий класс, например, ivan
        return instance.__dict__[self.incoming_attr]  # Все атрибуты объекта
        # хранятся в словаре
        # Здесь мы не изменили поведение __get__, на выход метода отдали
        # входящее значение return instance.__dict__[self.incoming_attr]

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError("Тип данных должен быть int")
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        instance.__dict__[self.incoming_attr] = value  # Можно не писать эту
        # строку

    def __delete__(self, instance):
        del instance.__dict__[self.incoming_attr]

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr


class Person:
    age = PositiveNumber()  # Дескриптор = атрибут объекта со "связанным"
    # поведением
    phone = PositiveNumber()
    name = NameType()

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


class BankAccount:
    balance = PositiveNumber()  # Сопоставление идёт по имени, аргумент
    # передавать не нужно
    card_number = PositiveNumber()
    cardholder_name = NameType()

    def __init__(self, balance, card_number, cardholder_name):
        self.balance = balance
        self.card_number = card_number
        self.cardholder_name = cardholder_name


ivan = Person('Иван', 25, 123456)
stephan = Person('Степан12', 23, 6589)  # Ошибка типа данных - цифры в имени
ivan.age = 15

ivan_bank_account = BankAccount(50000, 123456789, "Ivan256")  # Ошибка типа
# данных в имени держателя карты
stephan_bank_account = BankAccount(80000, 236547852, "Stephan")
