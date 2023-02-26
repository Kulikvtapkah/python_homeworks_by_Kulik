"""Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import random


def input_number(invitation: str):
    tester = False
    while tester == False:
        try:
            number = float(input(invitation))
            tester = True
        except ValueError:
            invitation = "Хмм, вряд ли это число... Попробуйте еще раз >> "
    return number


def get_pos_in_range(some_list: list, bottom: int, top: int):
    pos_list = []
    for i, el in enumerate(some_list):
        if bottom <= el <= top:
            pos_list.append(i)
    return pos_list


random_list = [random.randint(-100, 100) for i in range(20)]
print(f"Случайный массив: {random_list}")
top = input_number("Введите верхнюю границу диапазона >> ")
bottom = input_number("Введите нижнюю границу диапазона >> ")
print(f"Элементы списка на позициях {get_pos_in_range(random_list, bottom, top)} попадают в диапазон.")
