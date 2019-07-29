#### DOSYA OKUMA ####

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

# Dosya okumanın kolay yolu open ve close fonksiyonlarını kullanamıza gerek kalmaz.
# İlk 4 karakterin okuma, boş bırakılırsa tamamını okur.
with open(example1, "r") as file1:
    print(file1.read(4))
   
#### DOSYA YAZMA ####

# Satır yazma
with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")
 
#### DOSYA KOPYALAMA ####
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
