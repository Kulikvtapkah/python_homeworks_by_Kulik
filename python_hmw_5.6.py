"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def input_number(invitation: str):
    try:
        number = int(input(invitation))
        return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")


def guessing_game(number: int, lives: int = 10,
                  invitation: str = "Включаем интуицию, читаем мысли машины... Ваш вариант >> "):
    guess = input_number(invitation)
    if number == guess:
        return f"Ура! Победа! Число {number} угадано с {11 - lives} попытки!"
    else:
        lives -= 1
        if lives > 0:
            if number < guess:
                print(f"Верное число меньше. Попыток осталось: {lives}, шанс есть, дерзайте!")
            else:
                print(f"Верное число больше. Попыток осталось: {lives}, шанс есть, дерзайте!")
            return guessing_game(number, lives, "Ваш вариант >> ")
        else:
            return f"Увы! Потеря потерь! Число  было {number}. В следующий раз повезет... но это не точно"


import random

print(guessing_game(random.randint(0, 100)))
