# Дано несколько чисел. Подсчитайте,
# сколько из них равны нулю, и выведите это количество.

N = int(input())
s = 0
for i in range(N):
    n = int(input())
    if n == 0:
        s += 1
print(s)
