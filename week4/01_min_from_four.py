# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if,
# а использует стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.

a, b = int(input()), int(input())
c, d = int(input()), int(input())
print(min(min(a, b), min(c, d)))
