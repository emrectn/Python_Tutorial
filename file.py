# Eğer dosya yoksa
try:
    file = open("info.txt", "r")
except FileNotFoundError:
    print("Dosya Bulunamadı")


# file üzerinde satır satır gezme
for i in file:
    print(i)
file.close()

# Tüm satırları listeye alma
liste = file.readlines()
file.close()