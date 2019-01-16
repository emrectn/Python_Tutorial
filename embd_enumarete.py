"""
Bu konuda enumerate fonksiyonunu öğrenmeye çalışacağız. enumerate fonksiyonunu
daha iyi anlamak için ilk önce şu örneğe bakalım.
"""

liste = ["Elma", "Armut", "Muz", "Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()
i = 0
for a in liste:
    sonuç.append((i, a))
    i += 1

print(sonuç)
# [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

"""
Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet
çiftleri oluşturuyoruz. for döngüsü yazarken bazen hem elemanları hem de
indeksleri almak isteyebiliriz. Böyle bir durumda numaralandırma işlemi yapan
enumerate fonksiyonunu kullanabiliriz.
"""

new_list = list(enumerate(liste))
print(new_list)
# [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

"""
Örneğin bir listenin çift indekslerini(0,2,4) enumerate kullanarak nasıl
yazdırabiliriz ? Hemen bakalım.
"""
liste = ["a", "b", "c", "d", "e", "f", "g"]

for index, eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ", eleman)

""" Sonuçlar """
# Eleman:  a
# Eleman:  c
# Eleman:  e
# Eleman:  g
