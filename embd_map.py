"""
    Iterasyon sağlanabilen herhangi bir yapıyı tek tek fonksiyona göndererek yeni bir map objesi yaratılmasını sağlar.
    Bu objeyi list veya dict ile değiştirebilir.
"""


liste = [1, 2, 3, 4, 5]


def double(x):
    return x * 2

new_liste = map(double, liste)

print("liste : ", liste)
print("new_liste : ", list(new_liste))

# Lambda kullanarak kare alma
new_liste = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(new_liste)

# 2 ayrı listeyi birbiriyle çarpma
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]

new_liste = list(map(lambda x, y: x*y, liste1, liste2))
print(new_liste)


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)

funcs = [multiply, add]

[0, 1, 2, 3, 4]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
