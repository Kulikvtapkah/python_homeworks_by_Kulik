"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, content=[[]]):
        self.content = content

    def __str__(self):
        lines = ''
        for i in range(len(self.content)):
            line = ''
            for j in range(len(self.content[i])):
                line += str(self.content[i][j]) + (5 - len(str(self.content[i][j]))) * ' '
            lines += f'{line}\n'
        return lines

    def __add__(self, other_matrix):
        sum_matrix = Matrix()
        if len(self.content) == len(other_matrix.content) and len(self.content[0]) == len(other_matrix.content[0]):
            for i in range(len(self.content)):
                current_line = []
                for j in range(len(self.content[0])):
                    current_line.append(self.content[i][j] + other_matrix.content[i][j])

                sum_matrix.content.append(current_line)
            return sum_matrix
        else:
            return ('Эти матрицы сложить нельзя(')


a = Matrix([[4, 77, 3], [2, 3, 66], [5, 188, 335]])
print(str(a))
b = Matrix([[1, 77, 3], [66, 3, 66], [5, 188, 9]])
print(str(b))

c = Matrix([[1, 77, 3], [66, 3, 66]])

print(f'Сумма матриц: {str(a + b)}')
print(f'Сумма матриц: {str(c + b)}')
