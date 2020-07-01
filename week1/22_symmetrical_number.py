'''
Дано четырехзначное число.
Определите, является ли его десятичная запись симметричной.
Если число симметричное, то выведите 1, иначе выведите любое другое целое число.
Число может иметь меньше четырех знаков,
тогда нужно считать, что его десятичная запись дополняется слева нулями.
'''
N = int(input().zfill(4))
a = N // 1000
b = (N - a * 1000) // 100
c = (N - a * 1000 - b * 100) // 10
d = N - a * 1000 - b * 100 - c * 10
print(0**((a - d)**2 + (b - c)**2))
