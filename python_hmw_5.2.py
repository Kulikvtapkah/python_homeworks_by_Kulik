"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def input_number(invitation: str):
    try:
        number = abs(int(input(invitation)))
        return number
    except ValueError:
        return input_number("Хмм, вряд ли это число... Попробуйте еще раз >> ")


def digits_counter(number: int, count_odds: int = 0, count_even: int = 0):
    digit = number % 10
    if digit % 2 == 0:
        count_odds += 1
    else:
        count_even += 1
    number //= 10
    if number > 0:
        return digits_counter(number, count_odds, count_even)
    else:
        return [count_odds, count_even]


number = input_number("Введите натуральное число >> ")
digit_count = digits_counter(number)
print(f'Количество нечетных цифр в числе {digit_count[0]} ')
print(f'Количество четных цифр в числе {digit_count[1]} ')
