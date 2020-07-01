'''
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек.
Определите размер вклада через год.
При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
'''
P, X, Y = int(input()), int(input()), int(input())
S = X * 100 + Y
R = S + P * S / 100
print(int(R // 100), int(R % 100))
