"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число."""

import random
n = int(input("Введите натуральное число N >> "))
if n < 0:
    n = abs(n)
    print(f"Количество не бывает отрицательным. Предлагаю N={n}.")
some_list = list()
for i in range(n):
    some_list.append(random.randint(-n, n))
print(f"Рандомный список: {some_list}.")
f = open("positions.txt")
pose_1 = int(f.readline())
pose_2 = int(f.readline())
if ((pose_1 or pose_2) < -n) or ((pose_1 or pose_2) > n-1):
    print(f"Позиции {pose_1} и {pose_2} вне списка")
else:
    print(f"Произведение чисел в позициях {pose_1} и {pose_2} = {some_list[pose_1] * some_list[pose_2]}")
