# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers_str = '1 2 3 4'

with open('new_file.txt', 'w') as f:
    f.write(numbers_str)

with open('new_file.txt', 'r') as f:
    content = f.read()
    content = list(map(int, content.split()))
    print(sum(content))
