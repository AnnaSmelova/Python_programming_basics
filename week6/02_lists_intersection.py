# Даны два списка, упорядоченных по возрастанию
# (каждый список состоит из различных элементов).
# Найдите пересечение множеств элементов этих списков,
# то есть те числа, которые являются элементами обоих списков.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Решение оформите в виде функции Intersection(A, B).
# Функция должна возвращать список пересечения данных
# списков в порядке возрастания элементов.
# Модифицировать исходные списки запрещается.


def intersection(a, b):
    c = []
    lnga = len(a)
    lngb = len(b)
    i, j = 0, 0
    for k in range(lnga + lngb):
        if i < lnga and j < lngb:
            if a[i] == b[j]:
                c.append(a[i])
                i += 1
                j += 1
            elif a[i] > b[j]:
                j += 1
            else:
                i += 1
    return c


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*intersection(l1, l2))