# Дан список целых чисел, число k и значение C.
# Необходимо вставить в список на позицию с индексом k элемент,
# равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
# Поскольку при этом количество элементов в списке увеличивается,
# после считывания списка в его конец нужно будет добавить новый элемент,
# используя метод append.
# Вставку необходимо осуществлять уже в считанном списке,
# не делая этого при выводе и не создавая дополнительного списка.


myl = list(map(int, input().split()))
k, c = list(map(int, input().split()))
a = ''
lng = len(myl)

if k >= lng:
    myl.append(c)
else:
    for i in range(k, lng):
        if i == k:
            a = myl[i]
            myl[i] = c
        else:
            myl[i], a = a, myl[i]
    myl.append(a)
print(*myl)
