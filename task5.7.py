# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

firm_list = ['firm_1 OOO 100000 50000', 'firm_2 OAO 10000 8000', 'firm_3 AO 10000 11000']

with open('new_file.txt', 'w') as f:
    for line in firm_list:
        f.write(line + '\n')

with open('new_file.txt', 'r') as f:
    profit_avg = 0
    profit_dict = {}
    for i in range(1, len(firm_list) + 1):
        str = f.readline()
        str = str.split()
        profit = int(str[2]) - int(str[3])
        profit_dict[str[0]] = profit
        if profit > 0:
            profit_avg = profit_avg + profit
        print(f'Прибыль компании {i}: {profit}')

profit_avg = round(profit_avg / len(firm_list))
print(f'Средняя прибыль: {profit_avg}')

avg_profit_dict = {}
avg_profit_dict['average_profit'] = profit_avg

result_list = [profit_dict, avg_profit_dict]
print(result_list)

with open('new.json', 'w') as f:
    json.dump(result_list, f)

