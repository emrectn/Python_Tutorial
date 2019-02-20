# Os modülü işletim sisteminde işlemler gerçekleştirebildiğimiz standard bir Python modülüdür.
import os

# Bu fonksiyon, bulunduğumuz dizinin yolunu söyler.
os.getcwd()
# 'C:\\Users\\user\\Desktop\\Sıfırdan İleri Seviyeye Python\\İleri Seviye Modüller'


# Bu fonksiyon , bulunduğumuz dizini değiştirmemizi sağlar.
os.chdir("C:/Users/user/Desktop")
os.getcwd()
# 'C:\\Users\\user\\Desktop'


# Bu fonksiyon, bulunduğumuz dizinde klasörleri ve dosyaları listeler.
os.getcwd()
print(os.listdir())
# ['.ipynb_checkpoints', 'bilgiler.txt', 'desktop.ini', 'eclipse', 'eclipse.lnk', 'Git Shell.lnk']


# Bu fonksiyon , "klasör" oluşturmamızı sağlar.
os.mkdir("Deneme1")


# Bu fonksiyon iç içe klasör oluşturmamızı sağlar.
os.makedirs("Deneme2/Deneme3/Deneme4")


# Bu fonksiyon, klasör silmemizi sağlar.
os.rmdir("Deneme1")


# Bu fonksiyon, iç içe klasörleri silmemizi sağlar.
os.removedirs("Deneme2/Deneme3")


# Bu fonksiyon, dosya ve klasörlerin ismini değiştirmemizi sağlar.
os.rename("test.txt","test2.txt") # Dosyamızın yeni ismi "test2.txt" oldu.

#'Videolar\\Demo\\51.mp4'
path = os.path.join('Videolar', 'Demo', '51.mp4')

# Dosyanın olup olmadığının kontrolu - return boolean
os.path.isdir('Videolar')
os.path.exists('Videolar\\Demo\\51.mp4')
os.path.isfile('Videolar\\Demo\\51.mp4')

# Src klasöründeki test.txt nin Dest klasöründe copy.text olarak kopyalanaması
src = os.path.join('Src', 'test.txt')
dest = os.path.join('Dest', 'copy.text')
os.rename(src, dest)

"""
    Bu fonksiyon belki de os modülünün içindeki en yararlı fonksiyonlardan bir tanesi. Bu fonksiyonumuz içine bir tane 
    dizin (veya klasör) verdiğimizde bunun altındaki tüm dizinleri , dosyaları sıralar ve alt dizinlere gidilecek bir 
    yer kalmayana kadar gider. os.walk() çıktısını görmek için for döngüsü kullanmaya çalışalım.
"""

for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):

    print("Şu anki dizin",klasör_yolu)
    print("Klasörler ",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")

# ÖRNEK CIKTI
"""
Şu anki dizin C:/Users/user/Desktop
Klasörler  ['.ipynb_checkpoints', 'eclipse', 'PyQt5 Dersleri', 'Python', 'Sqlite Veritabanı', 'Sıfırdan İleri Seviyeye Python', 'İleri Seviye Modüller']
Dosyalar ['bilgiler.txt', 'desktop.ini', 'eclipse.lnk', 'Git Shell.lnk', 'ideaIC-2017.1.3.exe', 'photothumb.db', 'PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x32-2 .exe', 'PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x32-2.exe', 'tetris.py', 'Thumbs.db', '~$CEM KARACA.pptx']
**********************************
Şu anki dizin C:/Users/user/Desktop\.ipynb_checkpoints
Klasörler  ['Kültür Mantarı', 'Python_Kursu', 'Python_Udemy', 'Yeni klasör', 'Ödevler']
Dosyalar ['Adsız (4).wma', 'code.txt', 'Comparison Operators-checkpoint.ipynb', 'deneme.py', 'MustafaMuratCoskun_HizmetDokumu.pdf', 'Object Oriented Programming-checkpoint.ipynb']
**********************************
"""