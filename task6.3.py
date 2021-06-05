# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Woker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


    def incom_f(self, wage, bonus):
        self._incom = wage + bonus
        return {"wage": wage, "bonus": bonus}


class Position(Woker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self, wage, bonus):
        super().incom_f(wage, bonus)
        print(self._incom)


physician = Position('Ivan', 'Ivanov', 'therapist')
physician.get_full_name()
physician.get_total_income(150000, 50000)
print(physician.incom_f(150000, 50000))

surgeon = Position('Petr', 'Petrov', 'travmatologist')
surgeon.get_full_name()
surgeon.get_total_income(200000, 30000)
print(surgeon.incom_f(200000, 30000))
