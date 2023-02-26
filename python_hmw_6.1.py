"""Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""


def input_number(invitation: str):
    tester = False
    while tester == False:
        try:
            number = float(input(invitation))
            tester = True
        except ValueError:
            invitation = "Хмм, вряд ли это число... Попробуйте еще раз >> "
    return number


def input_n(invitation: str):
    tester = False
    while tester == False:
        n = input_number(invitation)
        if n < 0 or n % 1 != 0:
            invitation = "Нужно целое положительное число... Попробуйте еще раз >> "
        else:
            tester = True
    return int(n)


def progression_array(a1: float, n: int, d: float):
    progression_array = [a1]
    for i in range(n - 2):
        progression_array.append(a1 + (i + 1) * d)
    return progression_array

a1 = input_number("Введите первый элемент прогрессии >> ")
n = input_n("Введите количество элементов прогрессии >> ")
d = input_number("Введите разность прогрессии >> ")
print(f"Результат: {progression_array(a1, n, d)}")
