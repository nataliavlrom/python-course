# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = list(input("Введите элементы списка: "))
print(user_list)
user_list1 = user_list[::2]
user_list2 = user_list[1::2]
my_list = []

for elem in range(len(user_list) // 2):
    my_list.append(user_list2[elem])
    my_list.append(user_list1[elem])

if len(user_list) % 2 > 0:
    my_list.append(user_list[-1])

print(my_list)