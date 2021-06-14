# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    counter = 0


class Technol:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Printer(Technol):
    def __init__(self, amount, price, brand):
        super().__init__(amount, price)
        self.brand = brand


class Scaner(Technol):
    def __init__(self, amount, price, brand):
        super().__init__(amount, price)
        self.brand = brand


class Xerox(Technol):
    def __init__(self, amount, price, brand):
        super().__init__(amount, price)
        self.brand = brand


test = Xerox(4, 8000, 'hp')


