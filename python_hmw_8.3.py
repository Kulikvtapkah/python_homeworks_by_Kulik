"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

chess_importance = {'chess set': ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king'],
                'total number': 8,
                'piece value': {'pawn': '1 \u20AC',
                                'rook': '5 \u20AC\u20AC\u20AC\u20AC\u20AC',
                                'knight': '3 \u20AC\u20AC\u20AC',
                                'bishop': '3 \u20AC\u20AC\u20AC',
                                'queen': '9 \u20AC\u20AC\u20AC\u20AC\u20AC\u20AC\u20AC\u20AC\u20AC',
                                'king': 'priceless \u00AE\u20AC'}
                }
# Хотела вместо евро поставить знаки шахматных фигур. Нарвалась на ошибку, не нашла, как исправить(
# Как-то так пыталась:
# {'pawn': '1 \u2659',  'rook':'5 \u2656','knight': '3 \u2658',
# 'bishop': '3 \u2657', 'queen': '9 \u2655', 'king': 'priceless \u2654 '}

with open('chess.yaml', 'w') as f_n:
    yaml.dump(chess_importance, f_n, allow_unicode=True, sort_keys=False,)

with open('chess.yaml') as f_n:
    print(f_n.read())
