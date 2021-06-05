# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class PoliceCar(Car):
    pass


my_auto = Car(70, "red", "Mazda", False)
print(my_auto.__dict__)
print(my_auto.speed)
my_auto.go()
my_auto.stop()
my_auto.turn('право')
my_auto.show_speed()

print("_____________>")

town_auto = TownCar(50, "green", "Lada", False)
print(town_auto.__dict__)
print(town_auto.speed)
town_auto.go()
town_auto.stop()
town_auto.turn('право')
town_auto.show_speed()

print("_____________>")

sport_auto = SportCar(150, "yellow", "Ferrari", False)
print(sport_auto.__dict__)
print(sport_auto.speed)
sport_auto.go()
sport_auto.stop()
sport_auto.turn('лево')
sport_auto.show_speed()

print("_____________>")

work_auto = WorkCar(50, "whigt", "bob-cat", False)
print(work_auto.__dict__)
print(work_auto.speed)
work_auto.go()
work_auto.stop()
work_auto.turn('лево')
work_auto.show_speed()

print("_____________>")

police_auto = PoliceCar(100, "blue", "Ford", True)
print(police_auto.__dict__)
print(police_auto.speed)
police_auto.go()
police_auto.stop()
police_auto.turn('лево')
police_auto.show_speed()