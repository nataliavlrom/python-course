# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

lines = []
while True:
    user_str = input('Введите данные: ')
    lines.append(user_str)
    if not user_str:
        break
print(lines)

with open('new_file.txt', 'w') as f_new:
    for line in lines:
        f_new.write(line + '\n')
