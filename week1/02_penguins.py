'''
Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
Изображение одного пингвина имеет размер 5×9 символов
между двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего пингвина.
Для упрощения рисования скопируйте пингвина из примера в среду разработки.
'''
n = int(input())
penguin1 = '   _~_    '
penguin2 = '  (o o)   '
penguin3 = ' /  V  \  '
penguin4 = '/(  _  )\ '
penguin5 = '  ^^ ^^   '
print(penguin1 * n)
print(penguin2 * n)
print(penguin3 * n)
print(penguin4 * n)
print(penguin5 * n)
