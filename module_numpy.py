import numpy as np

a = [0,1,2,3,4]
# Numpy array oluşturma
np_a = np.array(a)
# Boyut ögrenme
np_a.size

u = np.array([1,0])
v = np.array([0,1])

# Karşılıklı satır satır toplanır. Concanete edilmez.
z = u + v # [1, 1]
z = u - v # [1,-1]

# *2 Her eleman 2 ile çarpılır.
v = [3,4]
z = 2*y # [6, 8]

# 2 listenin birbiriyle çarpılması.
u = [1,2]
v = [3,5]
z = u * v # [3, 10]

# +1 her elemana 1 eklenir.
u = [1,2]
z = u + 1 # [2,3]

# ortalama
mean_u = u.mean()

# max
u.max()

# line space - başlangıc ve bitiş sayılarını x parçaya bölme
np.linespace(-2,2,num=9)