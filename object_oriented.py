class Araba():
    '''
        Self methodu mevcut objeyi gösteren referanstır
        Her Fonksiyonun başında mutlaka olması gerekir.

    '''

    # Contructor - Obje oluşturulurken otomatik çalışır
    def __init__(self, marka, model, yıl):
        print('Yeni bir araba oluşturuldu')
        self.marka = marka
        self.model = model
        self.yıl = yıl

    def show_car_information(self):
        print("""Araba Markası : {} Model: {} Yılı : {}"""
              .format(self.marka, self.model, self.yıl))

araba = Araba('BMW', '320d', 2018)