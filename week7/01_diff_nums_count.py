# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.

a = list(map(int, input().split()))
s = set(a)
print(len(s))