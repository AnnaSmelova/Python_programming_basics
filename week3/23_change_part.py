'''
Дана строка.
Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.
'''
s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')
s = s[:pos1 + 1] + s[pos1 + 1: pos2].replace('h', 'H') + s[pos2:]
print(s)