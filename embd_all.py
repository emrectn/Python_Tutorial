def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True, False, True, False, True]

hepsi(liste)
# En az birisi False

# Daha önceden biliyoruz. 0' haricinde bütün sayılar True sayılmaktadır.
liste = [1, 2, 3, 4, 5]
hepsi(liste)
# Hepsi True


# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.
def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

liste = [True, False, True, False, True]
herhangi(liste)
# True

# Bütün değerler False , 0 = False
liste = [0, 0, 0, 0, 0, 0, 0]
herhangi(liste)
# False


"""
Aslında bu işlemleri all() ve any() fonksiyonları yapmaktadır.
İsterseniz bunların örneklerine bakalım.
all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False
sonuç döndürür.
"""