'''
Дана строка.
Удалите из нее все символы, чьи индексы делятся на 3.
Символы строки нумеруются, начиная с нуля.
'''
s = input()
k = ''
for i in range(len(s)):
    if i % 3 != 0:
        k += s[i]
print(k)
