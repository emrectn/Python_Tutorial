class Çalışan():
    def __init__(self, isim, soyisim, maaş):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş

    # obje çağırıldığında dönen bilgileri gösterir
    def __str__(self):
        return "\tİsim : {},\n\tSoyisim : {},\n\tMaaş : {}".format(
            self.isim, self.soyisim, self.maaş)

çalışan = Çalışan('emre', 'cetin', 2000)
print(çalışan)
del(çalışan)

# Olmadığı için hata vericek çünkü yukarıda silindi.
print(çalışan)