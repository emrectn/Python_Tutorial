"""
    İleri Seviye Karakter Dizileri (Stringler)
"""

"""
    upper() metodu stringin tüm karakterlerini büyük harfe çevirir.
    lower() metodu stringin tüm karakterlerini küçük harfe çevirir.
"""
"python".upper()
# 'PYTHON'

"PytHon".lower()
# 'python'


"""
    replace()
    replace(x,y) : Stringteki x değerlerini y ile değiştirir.
"""
"Herkes ana baba bacı gardaş".replace("a", "o")
# 'Herkes ono bobo bocı gordoş'

"Kunduz".replace("duz", "zun")
# 'Kunzun'


"""
    startswith() ve endswith()
    startswith(x) : String x ile başlıyorsa True, başlamıyorsa False döndürür.
    endswith(x) : String x ile bitiyorsa True, bitmiyorsa False döndürür.
"""

"Python".startswith("py")
# False

"Python".startswith("Py")
# True

"Python".endswith("on")
# True


"""
    split()
    split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir
    parça listeye atılır.
"""

# Boşluk karakterine göre ayrıldı.
liste = "Python Programlama Dili".split(" ")
print(liste)
# ['Python', 'Programlama', 'Dili']

liste2 = "Python-Php-Java-C-Javascript".split("-")
print(liste2)
# ['Python', 'Php', 'Java', 'C', 'Javascript']


"""
    strip() , lstrip() ve rstrip()
    strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.
    lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.
    rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.
"""

# değer göndermezsek varsayılan olarak boşluk karakteri
"                   python                          ".strip()
# 'python'

">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")
# 'Mustafa'

"                            python      ".rstrip()
# '                            python'


"""
    join()
    Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.
"""

liste = ["21", "02", "2014"]
"/".join(liste)
# '21/02/2014'

liste = ["T", "B", "M", "M"]
".".join(liste)
# 'T.B.M.M'

"""
    count()
    count(x): Stringin içindeki x değerlerini sayar.
    count(x,index): Stringin içindeki x değerlerini verilen index değerinden
    başlayarak saymaya başlar.
"""

"araba".find("a")
# 0

"araba".find("s")
# -1