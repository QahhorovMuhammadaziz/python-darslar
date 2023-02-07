def daraja(x):
    return x*x


def kg_gr(x):
    return x * 1000


def gr_kg(x):
    return x / 1000


def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)
