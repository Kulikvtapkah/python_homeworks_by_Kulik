"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    position = "просто царь"
    _income = {"wage": 123, "bonus": 456}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Новый сотрудник: {self.surname} {self.name}.")


class Position(Worker):
    def get_full_name(self):
        return f" {self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f'Cотрудник {self.get_full_name()} в должности \"{self.position}\", ' \
               f'суммарный доход: {self.get_total_income()} злт.'


boss = Position("Ilya", "Ivanov")
gold = boss.get_total_income()
print(f"Познакомьтесь, это {boss.get_full_name()}!")
print(f"ЗП сотрудника в должности \"{boss.position}\" согласно штатному расписанию: {gold} злт.")
print("")
lady_boss = Position("Анна", "Ыщ")
lady_boss.position = "жена царя"
lady_boss._income["wage"] = 10 * gold

print(str(lady_boss))
