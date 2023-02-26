"""Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc(num_1: float, num_2: float, operation: str):

    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        result = num_1 / num_2
    print(f'{num_1} {operation} {num_2} = {result}')
    return result


def input_number(invitation: str):
    try:
        number = float(input(invitation))
        return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")



def input_operation(invitation: str):
    operation = input(invitation)
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        return str(operation)
    else:
        return input_operation("Что-то пошло не так. Попробуйте еще раз (+, -, *, / ) >> ")


def zero_div_test (operation:str):
    num = input_number("Введите  второе число >> ")
    if num == 0 and operation == '-':
        print("Поделите на 0, получится бесконечность. Попробуйте другой делитель")
        return zero_div_test(operation)
    else:
        return float(num)

def calculator ():
    number_1 = input_number("Введите  первое число >> ")
    operation = input_operation("Введите  операцию (+, -, *, / ) >> ")
    number_2 = zero_div_test(operation)
    calc(number_1, number_2, operation)
    if input(f'Продожжим вычисления? (Enter для продолжения или введите любой знак для выхода) >> ') == '':
        print("Ура!")
        calculator()
    else:
        print("Пока!")

calculator()
