"""
    Bu konuda sayı veritiplerini biraz daha derinlemesine incelemeye ve sayılar
    üzerinde uygulanabilen yararlı fonksiyonları öğrenmeye çalışacağız. Bazen
    sayılar 'binary' ve  'hexadecimal' tabanda göstermek ve kullanmak istenir.
"""

# bin fonksiyonu sayımızı binary yazıldı.
bin(4)
# '0b100'

bin(19)
# '0b10011'

hex(32)
# '0x20'


"""
 FUNCTION

"""

# abs() -- Sayının mutlak değerini almamızı sağlar.
abs(-4)
# '4'

# round fonksiyonu -- Sayıları alta veya üste yuvarlar.
round(3.2123123123, 4) # 4 hanesine göre yuvarlar.

# max() ve min() -- en büyük ve en küçük döner
max(100, -2, 3, 4, 1, 131)
# '4'

min(100, -2, 3, 4, 1, 131)
# '-2'

# sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.
sum([3, 4, 5, 6, 7])
# '25'
sum((3, 4))
# '7'


# pow() fonksiyonu üs alma işlemlerinde kullanılır.
pow(2, 4) # 2 üzeri 4