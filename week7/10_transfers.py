# На Новом проспекте для разгрузки было решено пустить два
# новых автобусных маршрута на разных участках проспекта.
# Известны конечные остановки каждого из автобусов.
# Определите количество остановок,
# на которых можно пересесть с одного автобуса на другой.

ost = list(map(int, input().split()))
a1 = [ost[0], ost[1]]
a1.sort()
a2 = [ost[2], ost[3]]
a2.sort()
set1 = set(range(a1[0], a1[1] + 1))
set2 = set(range(a2[0], a2[1] + 1))
print(len(set1 & set2))
