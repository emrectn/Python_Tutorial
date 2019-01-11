from functools import reduce

"""
liste = [1, 2, 3, 4, 5]
 Reduce çalışma yapısı:
 liste[0] + liste[1] = 3
 3 + liste[2] = 6
 6 + liste[3] = 10
 10 + liste[4] = 15
"""


def toplama(x, y):
    return x + y

liste = [1, 2, 3, 4, 5]
new_liste = reduce(toplama, liste)
print(new_liste)


# Faktoriyel işlemi
new_liste = reduce(lambda x, y: x*y, liste)
print(new_liste)


# Maximum fonksiyonu
def maksimum(x, y):
    if (x > y):
        return x
    else:
        return y
print(reduce(maksimum, liste))
