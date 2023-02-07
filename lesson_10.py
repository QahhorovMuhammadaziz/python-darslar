
ism = input("Ismigiz nima?\n>>>")
if ism.lower() != 'ali':
    print(f"Uzr, {ism.title()} biz Alini kutyapmiz. ")
else:
    print("Salom, Ali")

javob = float(input("12x6 nechiga teng?>>>"))
if javob != 72:
    print("Javob xato")

yosh = int(input("Yoshingiz nechida?>>> "))
if yosh >= 18:
    print('Xush kelibsiz!')
else:
    print("kirish mumkun emas")

login = input("Yangi login tanlang: ")
if len(login) <= 5:
    print("Log in 5 harfdan ko'proq bo'lishi shart!")


yil = int(input("Tugulgan yiligizni kiriting: "))
if 2023-yil < 18:
    print(f"Yoshigiz {2023-yil}da ekan,")
    print("kirish mumkun emasa!")
else:
    print("Xush kelibsiz")
yosh = int(input("Yoshigiz nechida?>>>"))
if yosh > 60:
    print("Siz kattalar guruxida ekansiz")

x, y = 88, 60
print("x>y") if x > y else print("x<y")


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
else:
    print(car.title())


login = input("Login kiriting: ")
if login.lower() == 'admin':
    print("Xush kelibsiz Admin, foydalanuvchilar royhatini korsating ")
else:
    print(f"Xush kelibsiz {login.tiitle()} ")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"Sonlar teng: {x}={y}")


son = float(input("Istalga son kiriting:"))
print("Son manfiy") if son < 0 else print("Son musbat")
