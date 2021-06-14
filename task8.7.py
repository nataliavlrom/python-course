# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_num:

    def __init__(self, a, b):
        self.complex_num = complex(a, b)

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num

num1 = Complex_num(3, 4)
num2 = Complex_num(5, 6)

print(num1 + num2)
print(num1 * num2)
