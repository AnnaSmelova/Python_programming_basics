# Учительница задала Пете домашнее задание —
# в заданном тексте расставить ударения в словах,
# после чего поручила Васе проверить это домашнее задание.
# Вася очень плохо знаком с данной темой,поэтому он нашел словарь,
# в котором указано, как ставятся ударения в словах.
# К сожалению, в этом словаре присутствуют не все слова.
# Вася решил, что в словах, которых нет в словаре, он будет считать,
# что Петя поставил ударения правильно,
# если в этом слове Петей поставлено ровно одно ударение.
#
# Оказалось, что в некоторых словах ударение может быть поставлено больше,
# чем одним способом. Вася решил, что в этом случае если то,
# как Петя поставил ударение, соответствует одному из приведенных
# в словаре вариантов, он будет засчитывать это как правильную
# расстановку ударения, а если не соответствует, то как ошибку.
# Вам дан словарь, которым пользовался Вася и домашнее задание,
# сданное Петей.
# Ваша задача — определить количество ошибок,
# которое в этом задании насчитает Вася.


def check_word(word):
    w = list(word)
    kol = 0
    for s in w:
        if s.isupper():
            kol += 1
            if kol > 1:
                return 1
    if kol == 0:
        return 1
    return 0


n = int(input())
d = {}
for _ in range(n):
    word = input()
    k = word.lower()
    if k in d:
        d[k].append(word)
    else:
        d[k] = [word]
test = input().split()
err = 0
for w in test:
    if w.lower() in d:
        if w not in d[w.lower()]:
            err += 1
    else:
        err += check_word(w)
print(err)
