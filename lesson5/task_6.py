__author__ = 'Alex Bulavin'
# Очищаем консоль
os.system('clear')
import random

debug_mode = False  # True


def guess_number(rndm_num, attempts=10, min_edge=0, max_edge=100):
    if attempts == 0:
        print(f"Вы исчерпали все попытки. Загаданное число было", rndm_num)
        return
    guess = tm.recurse_input_natural(f"Угадайте число от {min_edge} "
                                     f"до {max_edge}: ",
                                     NOT_INT_POSITIVE_OR_TEXT, debug_mode)
    if guess == rndm_num:

        tm.output_dynamic_string(f"Вы угадали число c "
                                 f"{10 - attempts + 1} попыток!\n")
        attempts = 0
        return attempts
    elif guess < rndm_num:
        tm.output_dynamic_string(f"Загаданное число больше.")
        tm.output_dynamic_string(f"\nОсталось {attempts - 1} попыток")
        guess_number(rndm_num, attempts - 1, guess, max_edge)
    else:
        tm.output_dynamic_string(f"Загаданное число меньше.")
        tm.output_dynamic_string(f"\nОсталось {attempts - 1} попыток")
        guess_number(rndm_num, attempts - 1, min_edge, guess)


# Генерируем случайное число от 0 до 100
rndm_num = random.randint(0, 100)

# Запускаем игру
guess_number(rndm_num, 10, 0, 100)