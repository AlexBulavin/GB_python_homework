"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
<<<<<<< HEAD
=======
words = ["разработка", "администрирование", "protocol", "standard"]

# преобразование слов в байтовые строки
byte_words = [word.encode() for word in words]

# вывод байтовых строк
for i, byte_word in enumerate(byte_words):
    print(f"{words[i]} = {byte_word}")

# преобразование байтовых строк обратно в строки
decoded_words = [byte_word.decode() for byte_word in byte_words]

# вывод строковых представлений
for word in decoded_words:
    print(word)
>>>>>>> Lesson10
