# Дан список целых чисел. Требуется “сжать” его,
# переместив все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

a = list(map(int, input().split()))
lng = len(a)
i = 0
while i < lng:
    if a[i] == 0:
        a.pop(i)
        a.append(0)
        lng -= 1
    else:
        i += 1
print(*a)
