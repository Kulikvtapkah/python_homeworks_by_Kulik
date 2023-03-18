"""
Задание 4.

Преобразовать слова «разработка», ««администрирование»», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


word_list = ['разработка', '«администрирование»', 'protocol', 'standard']
print(f"Исходный массив: {word_list}")
for i in range (len(word_list)):
    word_list[i] = word_list[i].encode('utf-8')

print(f"После конвертации в байты: {word_list}")

for i in range (len(word_list)):
    word_list[i] = word_list[i].decode('utf-8')

print(f"После обратной конвертации: {word_list}")

