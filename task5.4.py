# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

text_list = ['One — 1', 'Two — 2', 'Three — 3', 'Four — 4']

with open('new_file.txt', 'w', encoding= 'UTF-8') as f:
    for line in text_list:
        f.write(line + '\n')

change_list = ['One', 'Two', 'Three', 'Four']
new_list = ['Один', 'Два', 'Три', 'Четыре']

with open('new_file.txt', 'r', encoding= 'UTF-8') as f:
    i = 0
    while i < len(text_list):
        content = f.readline()
        content = content.replace(change_list[i], new_list[i])
        print(content)
        i += 1
        with open('out_file.txt', 'a', encoding= 'UTF-8') as new_f:
            new_f.write(content + '\n')
