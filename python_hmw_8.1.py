"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import os
import re
import csv


def get_data_list(headers, info_file):
    data_list = list(range(len(headers)))
    with open(info_file, encoding='utf-8') as f_obj:
        for line in f_obj:
            for i in range(len(headers)):
                to_match = headers[i]
                if re.match(to_match, line):
                    data_list[i] = line[len(to_match)::].strip()
    return tuple(data_list)


def get_main_data(headers):
    directory = 'python_hmw_8.1'
    main_data_list = [headers]
    for file_name in os.listdir(directory):
        f = os.path.join(directory, file_name)
        main_data_list.append(get_data_list(headers, f))
    return tuple(main_data_list)


def write_to_csv(csv_data_file, data):
    with open(csv_data_file, 'w') as f_n:
        csv.writer(f_n).writerows(data)


headers_list = ('Изготовитель системы:', 'Название ОС:', 'Код продукта:', 'Тип системы:')

main_data = get_main_data(headers_list)
print(main_data)

write_to_csv('data_report.csv', main_data)
