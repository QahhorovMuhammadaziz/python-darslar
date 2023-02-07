print("Yaqin dos'stlarigizni royxatini tuzamiz.")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stigiz ismnini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrolash = input("yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrolash != 'ha':
        break
    print("Do'stlarigizni ro'yxati:")
for ism in ismlar:
    print(ism.title())
cars = ['lacetti', 'nexia', 'malibu', 'nexia', 'matiz', 'nexia']
car = 'nexia'
while car in cars:
    cars.remove(car)
print(cars)
savat = []
while True:
    mahsulot = input("Savatga mahsulot qoshing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q) ")
    if javob != 'ha':
        break


mahsulot = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting:")
    narh = input(f"{mahsulot.title()}ning narhini kiriting:")
    mahsulot[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != 'ha':
        break
