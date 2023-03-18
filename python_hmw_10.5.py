"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import os
import chardet

args_list = [['ping', 'youtube.com'], ['ping', 'youtube.com']]

for args in args_list:
    ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    print(ya_ping.stdout)
    for line in ya_ping.stdout:
        result = chardet.detect(line)
        print(line.decode(result['encoding']))



