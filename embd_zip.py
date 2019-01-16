"""
zip fonksiyonunu öğrenmeden önceden liste elemanlarını gruplamaya çalışalım
ve daha sonrasında zip fonksiyonunun faydasını görmeye çalışalım.
"""
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10, 11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i], liste2[i]))

    i += 1
print(sonuç)
# [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

"""
Peki böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ? İsterseniz zip
fonksiyonunun kullanımını direk örnek üzerinden görelim.
"""

zip_list = list(zip(liste1, liste2))
print(zip_list)

print("\n## Örnek 2 ##\n")
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
liste3 = ["Python", "Php", "Java", "Javascript", "C"]
print(list(zip(liste1, liste2, liste3)))

"""
Burada zip fonksiyonunun kullanımını görüyoruz. zip fonksiyonu listelerin
elemanları sırasıyla demet şeklinde gruplayarak bir tane liste oluşturuyor.
Başka bir örnek yapalım.
"""

# Aynı anda 2 liste üzerinde gezinmek için
print("\n## Örnek - 3 ##\n")

liste1 = [1, 2, 3, 4]
liste2 = ["Python", "Php", "Java", "Javascript"]

for i, j in zip(liste1, liste2):
    print("i:", i, "j:", j)

# i: 1 j: Python
# i: 2 j: Php
# i: 3 j: Java
# i: 4 j: Javascript

print("\n ## Sözlük Zipleme ## \n")
sözlük1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
sözlük2 = {"Sıfır": 0, "Bir": 1, "İki": 2}

# Anahtarlar eşleşti.
list(zip(sözlük1, sözlük2))
# [('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]

# Değerler eşleşti
list(zip(sözlük1.values(), sözlük2.values()))
# [(1, 0), (2, 1), (3, 2)]


print("\n## Örnek - 4 ##\n")
# unzipping values
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

namz, roll_noz, marksz = zip(*mapped)
