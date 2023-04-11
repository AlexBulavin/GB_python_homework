__author__ = 'Alex Bulavin'
'''
реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
'''
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    pass

a = MyClass()
b = MyClass()

print(a is b)  # True