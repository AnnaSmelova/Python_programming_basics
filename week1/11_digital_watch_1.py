'''
Дано число N.
С начала суток прошло N минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
'''
N = int(input())
K = N % (24 * 60)
print(K // 60, K % 60)
