"""Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
"""
import math

n = int(input("Введите натуральное N) >> "))
factor_set = set()
for i in range(2, n):
    while n % i == 0:
        factor_set.add(i)
        n = n / i
if n > 1:
    factor_set.add(n)
print(f"Список простых множителей: {factor_set}")
