'''
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
'''
n = int(input())
k = 0
x = n
while n != 0:
    if n > x:
        k += 1
    x = n
    n = int(input())
print(k)