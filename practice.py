def mijoz_inf(ism, familiya, tyil):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        'ism': ism,
        'familiya': familiya,
        'tyil': tyil,
        'yoshi': 2020-tyil,
    }
    return mijoz


def do_math():
    number = int(input("Enter your number: "))
    print(number, "ning kvadrati", number**2, "ga teng")
    print(number, "ning kubi", number**3, "ga teng")


def check_number():
    number = int(input("Enter any number: "))
    if number % 2:
        print(f"{number} toq son")
    else:
        print(f"{number} juft son")


def solishtir(number1, number2):
    number1 = int(input("Enter your number: "))
    if number1 > number2:
        print(f"{number1}>{number2}")
    elif number1 < number2:
        print(f"{number2}<{number1}")
    else:
        print(f"{number1}={number2}")


def daraja(x, n=2):
    print(f"{x} ning {n}-darajasi {x**n} ga teng")


def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
        matnlar[i] = matnlar[i].title()
        return matnlar


ismlar = ['ali', 'vali', 'hasan', 'husan']

ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)


talabalar = ["ali", "vali", "hasan", "husan"]


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
        baholar[ism] = baho
    return baholar


def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


def talaba_info(ism, familiya, **kwargs):
    kwargs['ism'] = ism
    kwargs['familiya'] = familiya
    return kwargs
