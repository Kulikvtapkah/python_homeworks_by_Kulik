"""Вычислить число pi c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
import math

d = len(input("Введите точность (до 10 знаков >> ")) - 2
print(round(math.pi, d))
