# Дана последовательность чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.


def get_n(s):
    n = int(input())
    if n != 0:
        s += n + get_n(s)
    return s

print(get_n(0))
