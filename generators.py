import types


# Basic
def test():
    print("emre")
    yield 1
    print("cetin")
    yield 2

for itreator_obje in test():
    print("----")


def gerisay(sayi):
    while sayi > 0:
        yield sayi
        sayi -= 1

print("3'ten geri sayiniz : ")
a = gerisay(3)
print(next(a))
print(next(a))
print(next(a))


# Fibonacci Örneği
def fibonacci():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b

# Fibonacci Test
if isinstance(fibonacci(), types.GeneratorType):
    print("\nGood, The fib function is a generator")

    step = int(input("How many step do you want to see ? : "))
    for n in fibonacci():
        print(n)
        step -= 1
        if step == 0:
            break
