'''
По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
'''
n = int(input())
S = 0
for i in range(n):
    S += 1 / ((i + 1)**2)
print(S)
