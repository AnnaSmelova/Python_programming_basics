import math

# Даны два действительных числа x и y.
# Проверьте, принадлежит ли точка с координатами(x,y) заштрихованному квадрату
# (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES,
# иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.
# Решение должно содержать функцию IsPointInSquare(x, y),
# возвращающую True, если точка принадлежит квадрату и False,
# если не принадлежит.
# Основная программа должна считать координаты точки,
# вызвать функцию IsPointInSquareи в зависимости от возвращенного
# значения вывести на экран необходимое сообщение.
# Функция IsPointInSquare не должна содержать инструкцию if.


def IsPointInSquare(x, y):
    fi = -math.pi / 4
    x1 = x * math.cos(fi) + y * math.sin(fi)
    y1 = -x * math.sin(fi) + y * math.cos(fi)
    a = round(1 / math.sqrt(2), 6)
    return -1 * a <= x1 <= a and -1 * a <= y1 <= a


e, f = float(input()), float(input())
if IsPointInSquare(e, f):
    print('YES')
else:
    print('NO')
