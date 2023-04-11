__author__ = 'Alex Bulavin'


class TypeMeta(type):
    a = None

    # Должен вернуть словарь для атрибутов класса
    @classmethod
    def __prepare__(metacls, name, bases):
        # print(f'Перегружаю prepare')
        return type.__prepare__(metacls, name, bases)

    # Должен создать и вернуть новый класс
    def __new__(cls, name, bases, dct):
        # print(f'Выделение памяти для класса {name}, '
        #       f'имеющего кортеж базовых классов {bases}, '
        #       f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)

    # Должен инициализировать созданный класс

    def __init__(cls, name, bases, dct):
        # print(f'Инициализация класса {name}')
        super(TypeMeta, cls).__init__(name, bases, dct)

    # Должен создать и вернуть экземпляр нового класса
    def __call__(cls, *args, **kwargs):
        # print(f'Перегрузка класса {args}, {kwargs}')
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
        return cls.a

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr


class DocMetaTest(type):
    """
    Метакласс, проверяющий наличие документации в подконтрольном классе
    """

    def __init__(self, clsname, bases, clsdict):
        # Здесь clsname - имя класса
        # bases - родительский класс
        # clsdict - интерфейс класса, то есть методы и атрибуты класса
        # print(clsdict.items())
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


class Combine(TypeMeta, DocMetaTest):
    pass


class MyClass(metaclass=Combine):
    """
    Документация должна быть здесь
    """

    def method_2(self):
        """
        Описание
        """
        print("Что-то пошло не так")

    pass


a = MyClass()
b = MyClass()

print(a is b)  # True
