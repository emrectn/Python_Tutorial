"""
    DateTime Modülü
    DateTime modülü Pythonda zaman ve tarih işlemleri için kullandığımız hazır bir modüldür.
"""

from datetime import datetime

# Şu anki zamanı alma - now()
şu_an = datetime.now()
print(şu_an)
# 2017-07-11 17:01:36.472991

# Yılı ve ayı alıyoruz.
print(şu_an.year, şu_an.month)

# Şu anki zamanı daha güzel göstermek için ctime() fonksiyonunu kullanabiliriz.
print(datetime.ctime(şu_an))

"""
   Peki şu anki zamanın yıl, ay , gün gibi özelliklerin sadece belli bir kısmını nasıl gösterebiliriz ? Bunun için de strftime fonksiyonunu kullanacağız. 
   strftime() fonksiyonu
   
   Yıl bilgisini almak için : %Y
   Ay ismini almak için : %B
   Gün ismini almak için : %A
   Saat bilgisini almak için : %X
   Gün bilgisini almak için : %D

"""

şu_an = datetime.now()
print(datetime.strftime(şu_an, "%Y"))
# 2017
print(datetime.strftime(şu_an, "%B"))
# July
print(datetime.strftime(şu_an, "%A"))
# Tuesday
print(datetime.strftime(şu_an, "%X"))
# 17:10:14
print(datetime.strftime(şu_an, "%D"))
# 07/11/17
print(datetime.strftime(şu_an, "%Y %B %A"))
# 2017 July Tuesday

"""
    timestamp() ve fromtimestamp()
    Şu anki zamanı saniye cinsinden bulmak için, datetime objemizi (şu_an objesi) timestamp() fonksiyonumuza 
    gönderebiliriz. Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine 
    çevirebiliriz.
"""

print(datetime.timestamp(şu_an))
# 1499782214.253746

zaman =  datetime.fromtimestamp(1499782214.253746)
# 2017-07-11 17:10:14.253746