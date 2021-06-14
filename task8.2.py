# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_zero_err(Exception):
    def __init__(self, text):
        self.text = text


num1 = input('Введите число: ')
num2 = input('Введите число отличное от нуля: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise My_zero_err('На ноль делить нельзя!')
except My_zero_err as error:
    print(error)
except ValueError:
    print('Вы ввели не число')
else:
    print(num1 / num2)

