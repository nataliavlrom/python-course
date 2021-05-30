# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def f_division():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        return

    try:
        result = num1 / num2
    except ZeroDivisionError:
        return
    return result

print(f_division())
