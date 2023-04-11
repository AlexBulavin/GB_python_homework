__author__ = 'Alex Bulavin'


class Meta1(type):
    def __init__(cls, name, bases, attrs):
        print("Meta1")
        super().__init__(name, bases, attrs)


class Meta2(type):
    def __init__(cls, name, bases, attrs):
        print("Meta2")
        super().__init__(name, bases, attrs)


class CombinedMeta(Meta1, Meta2):
    pass


class MyClass(metaclass=CombinedMeta):
    pass


test1 = MyClass()
