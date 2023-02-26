"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def input_number(invitation: str):
    try:
        number = int(input(invitation))
        if number < 0:
            number = abs(number)
            print(f'Количество не бывает отрицательным(. Пусть будет {number}')
        return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")


def sequence_sum (number: int, sum: float = 0, current_val: float = 1):
    sum += current_val
    current_val /= -2
    number -= 1
    if number > 0:
        return sequence_sum (number, sum, current_val)
    else:
        return sum


number = input_number("Введите число >> ")

print(f'Сумма {number} элементов ряда = {sequence_sum(number)}. ')
