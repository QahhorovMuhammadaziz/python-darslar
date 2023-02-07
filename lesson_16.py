car0 = {
    'model': 'lacceti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 150000,
    'km': 50000,
    'karobka': 'avtomat',
}
car = car0
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, {car['narh']}$")
car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2019,
    'narh': 500000,
    'km': 60000,
    'karobka': 'mexanika',
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2020,
    'narh': 170000,
    'km': 40000,
    'karobka': 'avtomat',
}

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rang']} rang,"
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[0]['model'])

malibus = []
for n in range(10):
    new_car = {
        'model': 'malibu',
        'rang': None,
        'yil': 2020,
        'narh': None,
        'km': 0,
        'korobka': 'avto'
        }
    malibus.append(new_car)
    for malibu in malibus[:3]:
        malibu['rang'] = 'qizil'
        print(malibu)

    car2 = {
        'model': 'gentra',
        'rang': 'qizil',
        'yil': 2020,
        'narh': 170000,
        'km': 40000,
        'karobka': 'avtomat',
        }
navoiy = {'ism': 'Alisher Navoiy',
          'tyil': 1441,
          'vyil': 1501,
          'tjoy': "Xirot",
          'asarlar': ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", 'Munojot']
          }

buxoriy = {'ism': 'Abu Abdulloh Muhammad ibn Ismlom',
           'tyil': 810,
           'vyil': 870,
           'tjoy': 'Buxoro',
           'asarlar': ["Al-jome' as-sahih", "Al-adab al-mufrad", "Al-tarix "
                       "At-tarix as-sag'ir"]
           }
qodiriy = {'ism': 'Abdulla Qodiriy',
           'tyil': 1894,
           'vyil': 1938,
           'tjoy': 'Toshkent',
           'asarlar': ["O'tgan kunlar", "Mehrobdan Chayon", 'Obit ketmon']
           }

vohidov = {'ism': 'Erkin Vohidov',
           'tyil': 1936,
           'vyil': 2016,
           'tjoy': 'Fargona',
           'asarlar': ["Tong nafasi", "Qo'shiqlar sizga", "O'zbegim"
                       "Qiziquvchan Matmusa"]
           }

navoiy = {'ism': 'Alisher Navoiy',
          'tyil': 1441,
          'vyil': 1501,
          'tjoy': "Xirot",
          'asarlar': ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", 'Munojat']
          }
shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari:")
    for asar in asarlar:
        print(asar)


kinolar = {
  'ali': ['Teminator', 'Rambo', 'Titanik'],
  'vali': ['Tenet', 'Inception', 'Interstellar'],
  'hasan': ['Abdullajon', 'Bomba', 'Shaytanat'],
  'husan': {'Mahallada duv-duv gap', 'John Wick'}
    }
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
for kino in kinolar:
    print(kino)


kinolar = {
   'Ali': ['Terminator', 'Rambo', 'Titanik'],
   'vali': ['Tenet', 'Invepition', "Interstellar"],
   'hasan': ['Abdullajon', 'Bomba', 'Shaytanat'],
   'husan': ['Mahallada duv-duv gap', 'John Wick']
 }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
for kino in kinolar:
    print(kino)


davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm"
    },
    "rossiya": {
        "poytaxt": "maskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl"
        },
    "aqsh":
        {"poytaxt": "vashintong",
         "maydon": 9_631_418,
         "aholi": 327_000_000,
         "pul birligi": "dollar"
         },

    "polsha":
        {" poytaxt": "varshava",
         "maydon": 312_7_000,
         "aholi": 38_5_000,
         "pul birligi": "polsha złoty",
         },
            }
# for davlat, info in davlatlar.items():
#     if davlat.lower() == "aqsh":
#         davlat = davlat.upper()
# else:
#     davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti{info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti{info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\npul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida malumot mavjud emas")
