"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

bytes_word_list = (b'class', b'function', b'method')
word_list = ('class', 'function', 'method')

for i in range(len(bytes_word_list)):
    print(f"Слово в байтах: {bytes_word_list[i]}; "
          f"тип:{type(bytes_word_list[i])}; "
          f"длина:{len(bytes_word_list[i])}.")
    print(f"Слово в str: {word_list[i]}; "
          f"тип:{type(word_list[i])}; "
          f"длина:{len(word_list[i])}.\n")
