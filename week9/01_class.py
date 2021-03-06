# Реализуйте класс Matrix. Он должен содержать:
#
# Конструктор от списка списков. Гарантируется, что списки состоят из чисел,
# не пусты и все имеют одинаковый размер.
#
# Конструктор должен копировать содержимое списка списков,
# т. е. при изменении списков, от которых была сконструирована матрица,
# содержимое матрицы изменяться не должно.
#
# Метод __str__, переводящий матрицу в строку.
# При этом элементы внутри одной строки должны быть разделены знаками
# табуляции, а строки — переносами строк.
# После каждой строки не должно быть символа табуляции и в конце не
# должно быть переноса строки.
#
# Метод size без аргументов, возвращающий кортеж вида
# (число строк, число столбцов).
# Пример теста с участием этого метода есть в следующей задаче этой недели.

from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matr):
        self.body = deepcopy(matr)

    def __str__(self):
        result = ''
        body_lng = len(self.body)
        for k in range(body_lng):
            k_lng = len(self.body[k])
            for i in range(k_lng):
                result += str(self.body[k][i])
                if i != k_lng - 1:
                    result += '\t'
                elif k != body_lng - 1:
                    result += '\n'
        return result

    def size(self):
        return len(self.body), len(self.body[0])


exec(stdin.read())
