"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
<<<<<<< HEAD
=======
words = ['class', 'function', 'method']
byte_words = [bytes(word, 'utf-8') for word in words]

for byte_word in byte_words:
    print(type(byte_word))  # <class 'bytes'>
    print(byte_word)  # b'class', b'function', b'method'
    print(len(byte_word))  # 5, 8, 6
>>>>>>> Lesson10
