"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def input_number(invitation: str):
    try:
        number = int(input(invitation))
        return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")


def digit_revers(number: int, revercy: int = 0):
    digit = number % 10
    number = number // 10
    revercy = revercy * 10 + digit
    if number > 0:
        return digit_revers(number, revercy)
    else:
        return revercy


number = input_number("Введите число >> ")
sign = 1
if number < 0:
    sign = -1
    number = abs(number)
print(f'Реверс: {digit_revers(number) * sign} ')
