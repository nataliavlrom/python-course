# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

typle_list = []
name_list = []
prise_list = []
number_list = []
ed_list = []
i = 0
while i < 3:
    i += 1
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    number = int(input("Введите количество товара: "))
    ed = input("Введите единицу измерения товара: ")

    name_list.append(name)
    prise_list.append(price)
    number_list.append(number)
    ed_list.append(ed)

    my_dict = {"название": name, "цена": price, "количество": number, "ед": ed}
    my_typle = (i, my_dict)
    typle_list.append(my_typle)

print(typle_list)

ed_list = set(ed_list)
ed_list = list(ed_list)

analytics_dict = {"название": name_list, "цена": prise_list, "количество": number_list, "ед": ed_list}
print(analytics_dict)
