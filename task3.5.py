# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

my_str = input("Введите числовой ряд через пробел: ")
result = 0
while True:
    if my_str.upper().count("Q") == 1:
        my_list = (my_str.split())
        my_list.pop()
        my_sum = sum(list(map(lambda x: int(x), my_list)))
        result = result + my_sum
        print(f'Сумма всех введенных чисел = {result}')
        break
    else:
        my_list = (my_str.split())
        my_sum = sum(list(map(lambda x: int(x), my_list)))
        result = result + my_sum
        print(f'Сумма всех введенных чисел = {result}')
        my_str = input("Введите числовой ряд через пробел: ")
