import re
"""
re kütüphanesinde türkçe karakter sorunu yaşanmaktadır. Bunu gidermek için regex kütüphanesi pip 
install yapılarak yüklenilebilir veya aşağıda kullanacağım gibi türkçe karakterler dahail edilebilinir.

Alıştırma ve deneme yapmak için aşağıdaki websiteyi kullanabilirsiniz.
https://regex101.com/
"""



"""
.   - Tüm herşey (Yeni satır karakteri hariç)
\d  - Herhangi bir rakam (0-9)
\D  - Rakam olmayan herhangi bir karakter (0-9)

\w - Herhangi bir karakter (a-z, A-Z, 0-9, _)
\W - Karakter olmayan herhangi bir şey

\s - Herhangi bir boşluk karakteri (boşluk, tab, yeni satır)
\S - Boşluk karakteri olmayan herhangi bir şey

\b - Herhangi bir kelime sınırı (!/./?/ /,)
\B - Kelime sınırı herhangi bir şey

^ - String başlangıcı
$ - String sonu

[]      - Parantez içindeki herhangi biri eşleşenler
[^ ]    - Parantez içindeki herhangi biriyle eşleşMEYENler
|       - Or
( )     - Group

Quantifiers:
*       - 0 veya daha fazla
+       - En az 1 veya daha fazla
?       - 0 veya 1
{3}     - 3 Tane
{3,4}   - Adet aralığı (Minimum, Maximum)

"""


# TEST DATAMIZ

kunye = """

Adı: Kara Kedi
Bölümü: Bişişsel Bilimler
Doğum Tarihi: 23/07
Email: kara.kedi@metu.edu.tr
ID: 14146

Adı: Çığırtkan Koca Mırnav
Bölümü: Opera Koro
Doğum Tarihi: 24/12
Email: cigirtkan.koca.mirnav@gmail.com
ID: 84474

Adı: Patili Morkedi
Bölümü: Psikoloji
Doğum Tarihi: 19/09
Email: patilimorkedi
ID: 74125

Adı: Asiye Sarıpati
Bölümü: Psikoloji
Doğum Tarihi: 24/01
Email: asiyesaripati@gmail.com
ID: 28163


Adı: Sırman Kocakuyruk
Bölümü: Psikoloji
Doğum Tarihi: 04/07
Email: sirmankocakuyruk@gmail.com
ID: 64574

Adı: Minnoş Göbüşüleziz
Bölümü: Miyavoloji
Doğum Tarihi: 02/07
Email: minnos_kedi07@pat_imail123.com
ID: 54574
"""


corba = "1Aa_.!? b\nC2\t3"

# Eğer '+' kendisini arıyor olsaydık \+ olarak aramamız gerekirdi
# pattern = re.compile(r"\w\+")

# Herhangi bir 3 karakter yan yana
pattern = re.compile(r"\w{3}")
	# <_sre.SRE_Match object; span=(0, 3), match='1Aa'>

# Herhangi bir min 2 max 3 karakter yan yana
pattern = re.compile(r"\w{2,3}")
	# <_sre.SRE_Match object; span=(0, 3), match='1Aa'>
	# <_sre.SRE_Match object; span=(10, 12), match='C2'>

# Rakam ve ya boşluktan herhangi biri varsa al
pattern = re.compile(r"[\d\s]")
	# <_sre.SRE_Match object; span=(0, 1), match='1'>
	# <_sre.SRE_Match object; span=(7, 8), match=' '>
	# <_sre.SRE_Match object; span=(9, 10), match='\n'>
	# <_sre.SRE_Match object; span=(11, 12), match='2'>
	# <_sre.SRE_Match object; span=(12, 13), match='\t'>
	# <_sre.SRE_Match object; span=(13, 14), match='3'>

# ^Rakam veya boş
pattern = re.compile(r"[^\d\s]")
	# <_sre.SRE_Match object; span=(1, 2), match='A'>
	# <_sre.SRE_Match object; span=(2, 3), match='a'>
	# <_sre.SRE_Match object; span=(3, 4), match='_'>
	# <_sre.SRE_Match object; span=(4, 5), match='.'>
	# <_sre.SRE_Match object; span=(5, 6), match='!'>
	# <_sre.SRE_Match object; span=(6, 7), match='?'>
	# <_sre.SRE_Match object; span=(8, 9), match='b'>
	# <_sre.SRE_Match object; span=(10, 11), match='C'>

# Enaz 1 harf ve sonrasında 1 rakam
pattern = re.compile(r"[A-Za-z]+[\d]")
matches = pattern.finditer(corba)

for match in matches:
	print(match)
	# <_sre.SRE_Match object; span=(10, 12), match='C2'>


"""
	Regex Gruplar
"""

# Adı: [herhangibir harf dizisi] - türkçe karakter olmadığı için "çğışöü" olarak biz ekledik
pattern = re.compile(r"Adı: [A-Za-zçğışöü ]+")
	# <_sre.SRE_Match object; span=(2, 16), match='Adı: Kara Kedi'>
	# <_sre.SRE_Match object; span=(219, 238), match='Adı: Patili Morkedi'>
	# <_sre.SRE_Match object; span=(309, 328), match='Adı: Asiye Sarıpati'>
	# <_sre.SRE_Match object; span=(410, 432), match='Adı: Sırman Kocakuyruk'>
	# <_sre.SRE_Match object; span=(516, 539), match='Adı: Minnoş Göbüşüleziz'>

# Sadece Ad kısmını almak için gruplandırdık. Regex ile eşleşen ifadenin tamamı group(0), parantez içine aldığımız kısım group(1) dir.
pattern = re.compile(r"Adı: ([A-Za-zçğışöü ]+)")
matches = pattern.finditer(kunye)
for match in matches:
	pass
	# print("Regex ile Eşleşen Tamamı : ", match.group(0))
	# print("Grup 1 : ", match.group(1))
	# Regex il Eşleşen Tamamı :  Adı: Kara Kedi
	# Grup 1 :  Kara Kedi
	# Regex il Eşleşen Tamamı :  Adı: Patili Morkedi
	# Grup 1 :  Patili Morkedi
	# Regex il Eşleşen Tamamı :  Adı: Asiye Sarıpati
	# Grup 1 :  Asiye Sarıpati
	# Regex il Eşleşen Tamamı :  Adı: Sırman Kocakuyruk
	# Grup 1 :  Sırman Kocakuyruk
	# Regex il Eşleşen Tamamı :  Adı: Minnoş Göbüşüleziz
	# Grup 1 :  Minnoş Göbüşüleziz


"""
Email için bir regex yazalım:
(1)emrecetin(2)@(3)gmail(4).(5)com
(1) - [A-Za-z0-9\._-] - Büyük-küçük harfler + rakam + "._-" olabilir.
(2)  - @ işareti
(3) - [A-Za-z0-9\.] - Büyük küçük harfler + rakam + "." dan oluşan domain adı.
(4) - "."
(5) - [A-Za-z] Sadece harflerdne oluşan com-net-biz vs.
"""

# pattern = re.compile(r"[A-Za-z0-9\._-]+@[A-Za-z0-9\.]+\.[A-Za-z]+") Aşağıdakinin aynısını
pattern = re.compile(r"[\w\.-]+@[\w\.]+\.[A-Za-z]+")
matches = pattern.finditer(kunye)
for match in matches:
	print(match)
	# <_sre.SRE_Match object; span=(70, 91), match='kara.kedi@metu.edu.tr'>
	# <_sre.SRE_Match object; span=(176, 207), match='cigirtkan.koca.mirnav@gmail.com'>
	# <_sre.SRE_Match object; span=(374, 397), match='asiyesaripati@gmail.com'>
	# <_sre.SRE_Match object; span=(478, 504), match='sirmankocakuyruk@gmail.com'>
	# <_sre.SRE_Match object; span=(586, 616), match='minnos_kedi07@pat_imail123.com'>


# Aşağıdaki dataki fazla boşlukları ve yanlış karakterin değiştirilmesi, cümle aralarında bulunan büyük harfleri ve cümle başındaki 
# büyük olması gereken küçük harflerin düzeltilmesini sağlayacağız.

raw_data = """
Sırtı  ona  dönÜK  ve  Kayıtsızmı$  gibi  pencerenin  önÜnden  dı$arısını  izleyen  Karısına  baKtı.  Kollarını  
Kavu$turmu$,  bir  savunma  duru$u  ichinde,  yansısı  pencere  camına  vuruyor  ve  yÜzÜnÜn  chizgileri  belli  
belirsiz  de  olsa  sechilebiliyor.
Seni  anlamaK  gÜch,  dedi  Kadın.  Ses  tonu  yumu$aK  ve  sevecen  değil,  bir  tartı$maya 
  davetiye  chıKarır  gibi.  Beni 

   anlamaK  gÜchtÜr.  HerKesin  herKesi  anlaması  gÜchtÜr 
ve  herKesin  Kendini  anlaması  daha  gÜchtÜr.  Su  alan  teKnem  dibe  vurdu  sonunda.  Onun  ichin  gidiyorum. 
 chantasının  ba$ından  doğruldu.  Kadına  yaKla$ıp  uzla$macı  
bir  tavırla  Kollarını  onun  Kavu$turulmu$  Kollarına  doladı.  chenesini  omzuna  
yaslayıp  bir  sÜre  bo$  soKağa  baKtı.  Dı$arıda  yağmur  yağıyordu.  SoKaK  lâmbalarını  yansıtan  
asfalt  ı$ıl  ı$ıldı.  Kadın  hafifche  Kastı  Kendini,  bu  KucaKlamadan  rahatsız  olmu$  gibiydi.
"""

# Birden fazla ard arda gelen boşluk karakterleri tek bir boşluk karakteri ile değiştirildi.
corpus = re.sub(r"[\s]+", r" ", raw_data)

# $ işareti ş işaretine çevrildi
corpus = re.sub(r"\$", r"ş", corpus)

# ch karakteri ç ye dönüştürüldü
corpus = re.sub(r"ch", r"ç", corpus)

# metindeki Harf içindeki ÜKŞÇ harflerinin küçültülmesi, Cümlenin ilk harfi hariç
def lowK(x):
	return(x.group(1)+x.group(2).lower())

pattern = re.compile(r"([^!\.?]{2})([ŞÇÜK]+)")
corpus1 = pattern.sub(lowK, corpus)
# print(corpus)

# Farklı bir yöntemle çözelim
def lowN(x):
	return x.group(0).lower() 
# Öncelikle tüm büyük K-Ü harfleri büyütülür.
corpus = re.sub(r"([KÜ]{1})", lowN, corpus)

def upperK(x):
	# print("gr 0 : {}\ngr 1 : {}\ngr 2 : {}".format(x.group(0), x.group(1), x.group(2)))
	return x.group(1) + x.group(2).upper()

"""
Daha sonra öncesinde cümle bitiren noktalama işareti sonrasında 1 boşluk ve k-ü-ç geliyorsa büyütüldü.
()() iki parantezleme yapılarak 2 tane gruba ayrıldı. Grup 0 işleşen regex ifadesiniin tamamını belirtir gr1 ilk parantez grubunu
ikinci grp2 ikinci parantezle ayrılmış ifadeyi belirtir. Aşağıdaki regex ifadesine gööre cümle sonu karakterlerinden biriyle ?!.
eşleştikten sonra " " space karakter ve k-ü-ç harflerinden biri geliyorsa.

anlaşıldı. küçük kız ... ". k" ifadesi regexle yakalanır. 
yakalan ifade 2 gruptur. Boşluk karakterin görünmesi için --" "-- ile belirtildi.
". k" ifadesi regex ile yakalnır.
gr 0 : --. k--
gr 1 : --. --
gr 2 : --k--

şeklinde ifade edilir.  Yakalan ifade upperK() fonksiyonuna gönderilir. Ve Satır başı olduğu için harf büyütülür.
"""
corpus = re.sub(r"([!?\.]{1} )([küç])", upperK, corpus)
print(corpus)

# Verilen datasetteki emreler Çetin ile değiştirilmesini sağlayacağız
dataset = "Emre özlemi seviyor"
dataset = re.sub(r"[eE]mre", "Çetin", dataset)
print(dataset)
