"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "принтер",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order_to_add = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders1.json') as f_n:
        order_dict = json.load(f_n)
        print(type(order_dict))
        order_dict['orders'].append(order_to_add)
        print(order_dict)

    with open('orders1.json', 'w') as f_n:
        json.dump(order_dict, f_n, sort_keys=False, indent=4)


write_order_to_json('A horse', 'one', 'Kingdom', 'Richard the Third', '1591')
write_order_to_json('freedom', '1', 'some wishes of an old fisher\'s wife', 'Goldfish', 'someday')
write_order_to_json('Knowlede and Pleasure', 'unlimited', 'soul', 'Faust', '1587')
write_order_to_json('Legs', '2', '1 voice', 'Ariel', 'one_stormy_night')
write_order_to_json('forehead flick', '3', 'hard work', 'Balda', 'Sunday')
write_order_to_json('theater ticket', '1', 'New ABC-book', 'Buratino', 'one_summer_day')
write_order_to_json('leasure day', '1', 'one day of his life', 'Shreck', 'long_long_ago')
