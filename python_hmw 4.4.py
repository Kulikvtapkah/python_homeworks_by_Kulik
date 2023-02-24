"""Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

import random

k = int(input("Введите степень >> "))

coefficient = []
for i in range(k + 1):
    coefficient.append(random.randint(0, 100))
print(f"Список коэффициентов: {coefficient}")

polynomial = ''
for i, el in enumerate(coefficient):
    if el != 0:
        if k - i > 0:
            if el != 1:
                polynomial = (f"{polynomial}{el}*x")
            else:
                polynomial = (f"{polynomial}x")
            if k - i > 1:
                polynomial = (f"{polynomial}^{k - i}")
        else:
            if el != 1:
                polynomial = (f"{polynomial}{el}")
        polynomial = (f"{polynomial} + ")
print(f"{polynomial[:-3]} = 0")
f = open("polynomial.txt", "w")
f.write(f"{polynomial[:-3]} = 0")
f.close()

