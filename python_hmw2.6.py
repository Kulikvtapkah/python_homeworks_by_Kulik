"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11"""

number = float(input("Введите вещественное число >> "))
number = str(abs(number)).replace('.', '0')
digit_sum = 0
for digit in number:
    digit_sum += int(digit)
print(f"Сумма цифр числа = {digit_sum}.")
