"""Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.


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
                polynomial += f"{el}*x"
            else:
                polynomial += f"x"
            if k - i > 1:
                polynomial += f"^{k - i}"
        else:
            if el != 1:
                polynomial += f"{el}"
        polynomial += f" + "
print(f"{polynomial[:-3]} = 0")

f = open("polynomial.txt", "w")
f.write(f"{polynomial[:-3]} = 0")
f.close() """


def polynomial_to_list(polynomial: str):
    polynomial = polynomial[:-4].split(' + ')
    for i, el in enumerate(polynomial):
        polynomial[i] = el.split('*x^')
        if len(polynomial[i]) == 1:
            polynomial[i] = el.replace('x', '1').split('^')
            if len(polynomial[i]) == 1:
                polynomial[i] = el.replace('x', '1').split('*')
                if len(polynomial[i]) == 1:
                    polynomial[i].append('0')
    return polynomial


def polynomial_sum(p_1: list, p_2: list):
    poly_sum = []
    i = 0
    k = 0
    while i < len(p_1) and k < len(p_2):
        if int(p_1[i][1]) != int(p_2[k][1]):
            if int(p_1[i][1]) > int(p_2[k][1]):
                poly_sum.append(p_1[i])
                i += 1
            else:
                poly_sum.append(p_2[k])
                k += 1
        else:
            sum_item = str(int(p_1[i][0]) + int(p_2[k][0]))
            poly_sum.append([sum_item, p_1[i][1]])
            i += 1
            k += 1
    return poly_sum


def list_to_polynomial(poly: list):
    polynomial_str = ''
    for i, el in enumerate(poly):
        polynomial_str += f'{poly[i][0]}*x^{poly[i][1]} + '
    polynomial_str = polynomial_str.replace(' 1*x', ' x').replace('x^1 ', 'x ').replace('*x^0 ', ' ')[:-2] + '= 0'

    return polynomial_str

f = open("poly_1.txt", "r")
polynomial_1 = f.readline()
f = open("poly_2.txt", "r")
polynomial_2 = f.readline()

print(polynomial_to_list(polynomial_1))
b = polynomial_to_list(polynomial_1)
a = polynomial_to_list(polynomial_2)
print(a)
print(a[0][1])
print(polynomial_sum(a, b))
print(list_to_polynomial(polynomial_sum(a, b)))

f = open("poly_sum.txt", "w")
f.write(list_to_polynomial(polynomial_sum(a, b)))
f.close()