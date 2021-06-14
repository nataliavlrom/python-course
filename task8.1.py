# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_int(cls, date):
        print(cls, list(map(int, date.split('-'))))

    @staticmethod
    def validation(date):
        date_list = list(map(int, date.split('-')))
        if date_list[0] in range(1, 32) and date_list[1] in range(1, 13):
            print('Все верно!')
        else:
            print('Дата введена некорректно')


Date.convert_int('09-06-2021')
Date.validation('09-06-2021')
Date.validation('32-06-2021')
Date.validation('09-00-2021')
