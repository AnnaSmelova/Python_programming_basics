'''
Улитка ползет по вертикальному шесту высотой H метров,
поднимаясь за день на A метров,
а за ночь спускаясь на B метров.
На какой день улитка доползет до вершины шеста?
'''
H = int(input())
A = int(input())
B = int(input())
print((H - A) // (A - B) + (1 - 0**((H - A) % (A - B))) + 1)
