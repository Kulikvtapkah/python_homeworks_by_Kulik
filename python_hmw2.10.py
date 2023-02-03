"""""
Реализуйте алгоритм перемешивания списка."""

#Читала, что есть функция shuffle() для перемешивания как раз.
# Но подумала, что "релизуйте алгоритм" означает, что надо свой создать
import random
expression =['о сколько', 'нам', 'открытий', 'чудных', 'готовит', 'просвещенья', 'дух']
print("Пушкин: " + ' '.join(expression).capitalize())
for i in range(len(expression)):
    mix_pos = (random.randint(0, len(expression) - 1 - i))
    expression.append(expression[mix_pos])
    expression.pop(mix_pos)
print("Yoda: " + ' '.join(expression).capitalize())


random.shuffle(expression)
print("Yoda: " + ' '.join(expression).capitalize())

