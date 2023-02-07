talaba_0 = {
    'ism': 'Muhammadaziz',
    'familiya': 'Qahhorov',
    'yosh': 18,
    'fakultet': 'TATU',
    "kurs":  1,
}
print(talaba_0['ism'])
print(talaba_0['yosh'])
print(talaba_0['fakultet'])
print(talaba_0.items())
for key, value in talaba_0.items():
    print(f"kalit : {key}")
    print(f"Qitmat : {value} \n")

telefonlar = {
     'Elmurod': 'samsumng A 53',
     'Nodirbek': 'mi 9',
     'Muhammadaziz': 'mi 5 plus',
     'sardorbek': 'samsumng A10',
     'ozodbek': 'redmi 7',
     'muzaffar': 'note 11',
     'humoyun': 'samsumng A12',
     'jamshid': 'iphone 4'
}
for k, q in telefonlar.items():
    print(f"{k.title()} ning telfoni {q}")

mahsulotlar = {
    'olma': 10000,
    'anor': 12000,
    'nok': 15000,
    'uzum': 40000,
    'shaftoli': 25000
}
print(mahsulotlar.keys())

print("Do\'kondagi mahsulotalr:")
for mahsulot in mahsulotlar:
    print(mahsulot.title())
bozorlik = ['olma', 'anor', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm ")


for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga  {buyum} ham olib keling")
print("Do'konimdagiz mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
print("Foydalanuvchilar quydagi telefonlarni ishlatadi:")
for tel in set(telefonlar.values()):
    print(tel)

davlatlar = {
    "o'zbekiston": 'toshkent',
    'aqsh': 'washington d.c.',
    'rossiya': 'moskva',
    'tojikiston': 'dushanbe',
    "qirg'iziston": 'bishkek',
    'qozog\'iston': 'nursulton',
    'malayziya': 'kuala-lumpur',
    'singapur': 'sungapur',
    'italiya': 'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)

if capital is None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")


python_words = {
    'integer': 'Butun son',
    'float': "O'lik son",
    'boolean': "Mantiqiy qiymat",
    'for': "Biror amalni qayta-qayta bajarish tsikli",
    'if': 'Shartlarni tekshirish operatori'
}

for key, value in sorted(python_words.items()):
    print(f"{key.title()}-  {value}")

menu = {
        'osh': 20000,
        "lag'mon": 22000,
        'non': 4000,
        'choy': 5000,
        'shashlik': 12000,
        'somsa': 6000,
        'tabaka': 15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
manu = {
    'somsa': 2000,
    'lagmon': 12000,
    'non': 4000,
    'choy': 5000,
    'shashlik': 8000,
    'tabaka': 15000
}
print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

    for buyurtma in buyurtmalar:
        if buyurtma in manu:
            print(f"{buyurtma.title()} {manu[buyurtma]} so'm")
else:
    print(f"Kechirasiz bizda {buyurtma} yoq")
