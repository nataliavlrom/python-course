# задание 2
time_seq = int(input("Число секунд: "))

if time_seq // 3600 >= 1:
    hour = time_seq // 3600
else:
    hour = 0

if (time_seq - (hour * 3600)) // 60 >= 1:
    min = (time_seq - (hour * 3600)) // 60
else:
    min = 0

seq = time_seq - (hour * 3600) - (min * 60)

print(hour, "чч: ", min, "мм: ", seq, "сс")

# Задание 3
# решение 1
number = int(input("Введите число от 1 до 9: "))
sum = number + (number + number * 10) + (number + number * 10 + number * 100)
print(sum)

# решение 2
number = int(input("Введите число от 1 до 9: "))
i = 0
newnumber = 0
sum = 0
while i <= 2:
    newnumber = newnumber + (number * (10 ** i))
    sum = sum + newnumber
    i = i + 1
print(sum)

# Задание 4
number = int(input("Введите целое положительное число: "))
max = 0
while number > 0:
    last_numeral = number % 10
    number = number // 10
    if last_numeral > max:
        max = last_numeral

print(max)

# Задание 5
revenue = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))

if revenue > cost:
    print("Фирма работает с прибылью")
    profitability = (revenue - cost)/revenue * 100
    print("Прибыль в процентах составила: ", profitability)
    employee_number = int(input("Введите число сотрудников фирмы: "))
    profitability_2 = (revenue - cost)/(revenue * employee_number) * 100
    print("Прибыль в процентах на одного сотрудника составила: ", profitability_2)
else:
    print("Фирма работает в убыток")

# Задание 6
a = int(input("Введите дистанцию первой пробежки, км.: "))
b = int(input("Введите дистанцию, которю хотели бы достигнуть, км. : "))

i = 0
while a < b:
    a = a + a * 0.1
    print(a)
    i += 1
i = i + 1
print(i)
