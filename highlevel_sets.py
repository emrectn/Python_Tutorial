"""
    İleri Seviye Kümeler (Sets)¶
    Bu konuda yeni bir veritipi olan kümeler(setleri) öğreneceğiz.
    Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir
    veritipidir.
"""


# Boş Küme oluşturmak
x = set()
type(x)
# set


# Aynı elemanı birçok defa  barındıran bir liste
liste = [1, 2, 3, 3, 1, 1, 2, 2, 2]
x = set(liste)
# Aynı elemanlar tek bir elemana indirgendi.
print(x)
# {1, 2, 3}


x = {"Python", "Php", "Python"}
# Aynı elemanlar tek bir elemana indirgendi.
print(x)
# {'Php', 'Python'}

"""
    Biz bir kümenin elemanlarına ne indexle ne de eleman ismiyle erişebiliyoruz.
    Erişmek için mutlaka veritipi dönüşümü yapmamız gerekiyor.
"""
liste = list({1, 2, 3, 4, 5})
liste[0]


"""
    Kümelerin Metodları
    Eleman Eklemek : add() metodu
    Kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez
    ve herhangi bir ekleme işlemi yapmaz.
"""

x = {1, 2, 3}
x.add(4)
print(x)
# {1, 2, 3, 4}

"""
    Kümeden Eleman Çıkartmak : discard() metodu
    İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu
    metod hiçbir şey yapmaz(Hata vermez).

"""

küme1 = {1, 2, 3, 4, 5, 6}
küme1.discard(2)
# küme1
# {1, 3, 4, 5, 6}


"""
    İki kümenin farkı : difference() metodu
    Bu metod birinci kümenin ikinci kümeden farkını döner.
    küme1.difference(küme2) # Küme1'in Küme2'den farkı
"""

küme1 = {1, 2, 3, 10, 34, 100, -2}
küme2 = {1, 2, 23, 34, -1}
küme1.difference(küme2)
# {-2, 3, 10, 100}

küme2.difference(küme1)
# {-1, 23}


"""
    İki kümenin farkı ve güncelleme : difference_update() metodu
    Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu
    farka göre günceller. küme1.difference_update(küme2) # Küme1'in Küme2'den farkı
"""

# küme1 {-2, 1, 2, 3, 10, 34, 100}
# küme2 {-1, 1, 2, 23, 34}
küme1.difference_update(küme2)
# küme1 Farka göre güncellendi.
# {-2, 3, 10, 100}


"""
    Küme kesişimleri : intersection() metodu
    Bu metod iki kümenin kesişimleri bulmamızı sağlar.
"""
küme1 = {1, 2, 3, 10, 34, 100, -2}
küme2 = {1, 2, 23, 34, -1}
küme1.intersection(küme2)
# {1, 2, 34}

"""
    Birleşim Kümesi : union() metodu
    Bu metod, iki kümenin birleşim kümesini döner.
"""

küme1 = {1, 2, 3, 10, 34, 100, -2}
küme2 = {1, 2, 23, 34, -1}
küme1.union(küme2)
# {-2, -1, 1, 2, 3, 10, 23, 34, 100}
