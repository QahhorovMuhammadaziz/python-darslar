def toliq_ism_yasa(ism, familiya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism


talaba2 = toliq_ism_yasa('Sardorbek', 'Abubakirov')
print(f"Darsga kelmagan talabalar: {talaba2} va {talaba2}")
print(f"{talaba2} darsga kechikib keldi.")


def toliq_ism_yasa(ism, familiya, otasini_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasini_ismi:
        toliq_ism = f"{ism} {otasini_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
        return toliq_ism.title()


talaba2 = toliq_ism_yasa('Muhammadaziz', 'Qahhorov', 'Shuhratbekovich')
print(f"Darsga kelmagan talaba: {talaba2} va {talaba2}")


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya': kompaniya,
            'model': model,
            'rang': rangi,
            'korobka': korobka,
            'yil': yili,
            'narh': narhi}
    return avto


avto = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra ', ' Oq', 'Mexanika', 2016, 15000)
avtolar = [avto, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


def oraliq(min, max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ismlar = ismlar.pop()
        baho = input(f"Talaba {ismlar.title()}ning bahosini kiriting: ")
        baholar[ismlar] = (baho)
    return baholar


ismlar = ['elmurod', 'sardor', 'ali', 'shoxrux']


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism': ism,
             'familiya': familiya,
             'tyil': tyil,
             'yoshi': 2020-tyil,
             'tjoy': tjoy,
             'email': email,
             'telefon': tel}
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2020 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print(mijoz_info)
