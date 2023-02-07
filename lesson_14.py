car_0 = {'model': 'ferariy', 'rang': 'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# en_uz = {'apple':'olma', 'apricot': "o'rik",'banana':"banan" }
# print(en_uz['apple'])
mevalar = {'olma': 10000, 'tarvuz': 8000, 'qovun': 10000}
print("olma narh {mevalar['olma']}som ")
talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000}
print(f"{talaba_0['ism'].title()},\
  {talaba_0['t_yil']}-yilda tu'gilgan,\
  {talaba_0['yosh']} yoshda")

talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'
talaba_0['ism'] = ('Abdulloh')


telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310'
    }

phone = telefonlar['ali']
print(f"Alining telefoni {phone}")
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")
phone = telefonlar.get('ali', 'Bunday ism mavjud emas')
print(phone)

otam = {'ismi': 'mavlutdin', 'tyil': 1954, 'viloyat': 'samarqand'}
tyil = otam['tyil']
vil = otam['viloyat']

print(f"Otamning ismi {otam['ismi'].title()} \n,{tyil}-yilda, {vil.title()} viloyatda tug'ilgan") # noqa
taomlar = {
    "ali": "osh",
    "vali": "shashlik",
    "hasan": "lag'mon",
    "husan": "mastava",
    "olim": "somsa"
    }

taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    'integer': "Butun son",
    'float': "O'nlik son",
    'string': "Matn",
    'list': "Ro'yxat",
    'tuple': "O'zgarmas ro'yxat"}
print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima is None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
otam = {'ismi': 'Shuxratbek', 'tyil': 1979, 'viloyat': 'andijon'}
tyil = otam['tyil']
vil = otam['viloyat']

print(f"Otamning ismi {otam['ismi'].title()}, \n{tyil}-yilda, {vil.title()} viloyatida tug'ilgan") # noqa
taomlar = {
    "ali": "osh",
    "vali": "shashlik",
    "hasan": "lag'mon",
    "husan": "mastava",
    "olim": "somsa"
}

taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")

otam = {'isim': 'Shuxratbek', 'tyil': 1979, 'viloyat': 'andijon'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi{otam['ismi']. title()}, \n{tyil}-yilda, {vil.title()} viloyatida tugulgan ") # noqa
