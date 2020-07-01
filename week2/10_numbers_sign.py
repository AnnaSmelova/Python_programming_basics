'''
В математике функция sign(x) (знак числа) определена так:

sign(x)=1, если x>0,

sign(x)=-1, если x<0,

sign(x)=0, если x=0.

Для данного числа x выведите значение sign(x).
'''
n = int(input())
if n < 0:
    print('-1')
elif n == 0:
    print('0')
else:
    print('1')
