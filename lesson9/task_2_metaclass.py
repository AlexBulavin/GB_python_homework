__author__ = 'Alex Bulavin'
'''
реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)

__prepare__() Должен вернуть словарь для атрибутов класса
__new__() вызывается для создания класса, должен создать и вернуть новый класс;
__init__() для инициализации класса, должен инициализировать созданный класс;
__call__() вызывается при создании объектов класса, должен создать и вернуть 
экземпляр нового класса;
'''


class SingletonMeta(type):
    _instances = {}

    # Должен вернуть словарь для атрибутов класса
    @classmethod
    def __prepare__(metacls, name, bases):
        print(f'Перегружаю prepare')
        return type.__prepare__(metacls, name, bases)

    # Должен создать и вернуть новый класс
    def __new__(cls, name, bases, dct):
        print(f'Выделение памяти для класса {name}, '
              f'имеющего кортеж базовых классов {bases}, '
              f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)

    # Должен инициализировать созданный класс

    def __init__(cls, name, bases, dct):
        print(f'Инициализация класса {name}')
        super(SingletonMeta, cls).__init__(name, bases, dct)

    # Должен создать и вернуть экземпляр нового класса
    def __call__(cls, *args, **kwargs):
        print(f'Перегрузка класса {args}, {kwargs}')
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DocMetaTest(type):
    '''
    Метакласс, проверяющий наличие документации в подконтрольном классе
    '''

    def __init__(self, clsname, bases, clsdict):
        # Здесь clsname - имя класса
        # bases - родительский класс
        # clsdict - интерфейс класса, то есть методы и атрибуты класса
        print(clsdict.items())
        for key, value in clsdict.items():  # В item будут находиться все
            # атрибуты и методы подчиненного класса
            if key.startswith('__'):  # Пропустить специальные и
                # частные функции
                continue

            if not hasattr(value, "__call__"):  # Пропустить любые называемые
                # объекты
                continue

            # Проверяем наличие строки документирования
            if not getattr(value, "__doc__"):
                raise TypeError(f'Метод {key} должен иметь описание, добавь')

        type.__init__(self, clsname, bases, clsdict)


class Combine(SingletonMeta, DocMetaTest):
    pass


class MyClass(metaclass=Combine):
    '''
    Документация должна быть здесь
    '''
    def method_2(self):
        '''
        Описание
        '''
        print("Что-то пошло не так")
    pass


a = MyClass()
b = MyClass()

print(a is b)  # True
