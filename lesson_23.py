def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya': kompaniya,
            'model': model,
            'rang': rangi,
            'korobka': korobka,
            'yil': yili,
            'narh': narhi}
    return avto


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end='')
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break


def info_print(avto_info):
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")


avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
