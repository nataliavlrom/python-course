# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

wokers_dict = {'Ivanov': 15000, 'Petrov': 75000, 'Sidorov': 50000}

with open('new_file.txt', 'w') as f:
    salary_sum = 0
    i = 0
    for key, value in wokers_dict.items():
        i += 1
        salary_sum = salary_sum + value
        f.write(f'{key} : {value} \n')
        if value < 20000:
            print(f'Сотрудник с окладом менее 20 тыс.: {key}')

mean_salary = round(salary_sum / i)
print(f'Средний доход: {mean_salary}')
