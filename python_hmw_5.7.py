"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def input_number(invitation: str):
    try:
        number = int(input(invitation))
        if number < 0:
            return input_number("Количество не бывает отрицательным. Попробуйте еще раз >> ")
        else:
            return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")


def progression_sum(n: int, sum: int = 0, show_string: str = ''):
    if n > 0:
        sum += n
        show_string = f"{n} + {show_string}"
        n -= 1
        return progression_sum(n, sum, show_string)
    else:
        return [sum, show_string]


def axiom_prove(n: int):
    print(f"Ну что, еще раз проверим аксиому... Для n = {n}:")
    print(
        f" {progression_sum(n)[1][:-2:]} = {n}({n}+1)/2 = {n * (n + 1) / 2}. Cнова {progression_sum(n)[0] == n * (n + 1) / 2}! ЧТД))) ")


axiom_prove(input_number(("Введите количество слагаемых n >> ")))
