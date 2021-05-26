#  Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#  У пользователя необходимо запрашивать новый элемент рейтинга.
#  Если в рейтинге существуют элементы с одинаковыми значениями,
#  то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
my_list_copy = [7, 5, 3, 3, 2]

number = int(input("Введите число: "))

my_list.reverse()

for n in my_list:
    if n == number:
        my_list.insert(n-1, number)
        break

my_list.reverse()

if my_list == my_list_copy:
    my_list.append(number)
    my_list.sort()
    my_list.reverse()

print(my_list)


