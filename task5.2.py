# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('new_file.txt', 'w') as f_new:
    str_list = ['one\n', 'two two\n', 'three three three\n']
    f_new.writelines(str_list)

with open('new_file.txt', 'r') as f_new:
    content = f_new.readlines()
    str_num = len(content)
    print(f'Число строк: {str_num}')

with open('new_file.txt', 'r') as f_new:
    i = 0
    for line in f_new:
        i += 1
        word_num = len(line.split())
        print(f'Число слов в {i} строке: {word_num}')
