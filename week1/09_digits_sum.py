'''
Дано трехзначное число.
Найдите сумму его цифр.
'''
N = int(input())
print(N // 100 + N // 10 % 10 + N % 10)
