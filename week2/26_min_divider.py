'''
Дано целое число, не меньшее 2.
Выведите его наименьший натуральный делитель, отличный от 1.
'''
N = int(input())
i = N
a = N
while i > 1:
    if N % i == 0:
        a = i
    i = i - 1
print(a)
