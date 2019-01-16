"""
    filter(fonksiyon, iterasyon yapabilen bir veritipi(liste cvb))
    return True, False
"""

""" False ise geri listeye ekleme yapmaz"""

# Çift mi Tek mi Kontrolu
liste = [1, 2, 3, 4, 5, 6]
new_list = filter(lambda x: x % 2 == 0, liste)
print(list(new_list))


ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)


"""-----------------------------------------------------"""


def asal_mi(x):
    i = 2
    if (x == 1):
        # Asal değil
        return False

    elif(x == 2):
        # Asal sayı
        return True

    else:
        while(i < x):
            if (x % i == 0):
                # Asal Değil
                return False
            i += 1

    return True

# 1 den 100' e kadar olan asal sayılar.
print("Hakan : ", list(filter(asal_mi, range(1, 100))))