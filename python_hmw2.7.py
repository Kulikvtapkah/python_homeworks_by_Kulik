"""
Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

number = int(input("Введите число N >> "))
if number > 0:
    multiple_set = set()
    current_multiple = 1
    for i in range(1, (number + 1)):
        current_multiple *= i
        multiple_set.add(current_multiple)
    print(f"Набор произведений от 1 до N: {multiple_set}.")
else:
    print("Только 1 и 0. Даже считать нечего(")

