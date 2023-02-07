import random as r


def daraja(n):
    return lambda x: x**n


kvadirat = daraja(2)
print(kvadirat(6))
kub = daraja(3)
print(kub())

sonnlar = list(range(11))
ildizlari = list(map(sonnlar))
print(ildizlari)
print(sonnlar)


def daraja2(x):
    """Berilgan sonni kvadiratini qaytaruvchi funksiya"""
    return x*x


print(list(map(daraja2, sonnlar)))

kvadratlar = list(map(lambda x: x*x, sonnlar))
print(kvadratlar)

a = [4, 5, 8]
b = [6, 3, 5]
a_plus_b = list(map(lambda x, y: x+y, a,  b))
print(a_plus_b)

sonlar = r.sample(range(100), 10)
print(sonlar)


def juftmi(x):
    return x % 2 == 0


juft_sonlar = list(filter(juftmi, sonlar))
print(juftmi(3))


