class Çalışan():
    def __init__(self, isim, soyisim, maaş):
        print("Çalışan sınıfı init fonksiyonu")
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş

    def bilgileri_göster(self):
        print("Çalışan sınıfı bilgileri")
        print("\tİsim : {},\n\tSoyisim : {},\n\tMaaş : {}"
              .format(self.isim, self.soyisim, self.maaş))

    def işten_çıkar(self):
        print('Çalışanlar işten çıkaramassın')


class Yönetici(Çalışan):

    # def __init__(self, isim, soyisim, maaş, çalışan_adedi):
    #     print("Çalışan sınıfı init fonksiyonu")
    #     self.isim = isim
    #     self.soyisim = soyisim
    #     self.maaş = maaş
    #     self.çalışan_adedi = çalışan_adedi

    '''
        Yöneticiler için ekstra çalışan_adedi özelliği kullanılmıştır.
        Yukarıdaki gibi __init__ fonksiyonunu override ederek tanımlanırsa,
        Çalışan ve Personel sınıfında isim, soyisim, maaş özellikleri tekrar
        eder. Bunun yerine super fonksiyonu kullanılır.
    '''

    def __init__(self, isim, soyisim, maaş, çalışan_adedi):
        print('Yönetici init fonksiyonu')
        super().__init__(isim, soyisim, maaş)
        self.çalışan_adedi = çalışan_adedi

    # Override edilip, diğer fonksiyona yeni şeyler eklendi
    def bilgileri_göster(self):
        super().bilgileri_göster()
        print('\tÇalışan adedi : {}'.format(self.çalışan_adedi))

    # Override edildi. (Kalıtım alınan fonksiyon iptal edildi.)
    def işten_çıkar(self):
        print('kimin çıkarılmasını istersin')


yönetici = Yönetici('emre', 'çetin', 2000, 10)
yönetici.bilgileri_göster()
print(yönetici)