# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    result_sum = sum(my_list) - min(my_list)
    return result_sum

print(my_func(3, 2, 1))