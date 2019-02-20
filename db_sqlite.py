import sqlite3

"""
    Python ile Sqlite Veritabanı nasıl kullanılır öğrenmeye çalışacağız. Bu bölümde basit anlamda Sqlite veritabanı 
    kodları bulunmaktadır.
"""

# Sqlite'yı dahil ediyoruz
import sqlite3

# Tabloya bağlanıyoruz.
con = sqlite3.connect("kütüphane.db")

# cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
cursor = con.cursor()


def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
    con.commit()

# INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)
def deger_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")
    con.commit()

# Peki kullanıcıdan aldığımız değerleri tabloya nasıl ekliyoruz ? Onun için de sorgumuzu ve kodumuzu biraz değiştireceğiz.
def kullanıcı_deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    data = cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.

def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?", ("Everest", yayınevi))
    con.commit()

def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?", (yazar,))
    con.commit()

# isim = input("İsim:")
# yazar = input("Yazar:")
# yayınevi = input("Yayınevi:")
# sayfa_sayısı = int(input("Sayfa Sayısı:"))

tablo_oluştur()
# deger_ekle()
# kullanıcı_deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)
verileri_al()
verileri_al3("Everest")
verigüncelle("Doğan Kitap")
verilerisil("Besen Ümit")

# Bağlantıyı koparıyoruz.
con.close()



