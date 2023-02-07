son = 66
if son<0:
    print("Kichik")
else:
    print("Kotta") 
yosh = int(input("Yoshigiz nechida?"))
if yosh<=4:
     print("Sizga kirish bepul")  
elif yosh<=12:
    print("Sizga kirish 5000 so\'m")
else:
    print("Sizga kirish 10000 so\'m")
yosh = int(input("Yoshigiz nechida?"))
if yosh < = 4 :
    narh = 0
elif yosh<=12:
    narh = 5000
elif yosh<= 18:
    narh = 8000
else:
  narh = 10000
   
  print(f"Sizga kirish {narh} so'm")
kun = input("Bugun qanaqa kun?>>>")
if kun.lower()=='bugun shanba' or kun.lower()=='yakshanba':
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni.")
kun= input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))

if kun.lower()=='yakshanba' and harorat>=30:
    print("Basenga kettik !")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz")
narh = 15000
choy = True
salat =False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
    print(f"Jami {narh} so'm")
menu = ['qozonkabop','shashlik','norin','somsa','lagmon']
ovqat = input("Nima ovqat yeysiz?>>>")
if ovqat.lower() in menu:
  print("Buyurtma qabul qilindi.")
else:  
    print("Afsuski bunday ovqat yo\'q")
1-amalyot
son = float(input("Juft soni kiriting"))
if son%2:
    print('Bu son juft emas')
else:
    print("Raxmat!")  
2-amalyot


mahsulotlar = ['un', 'yog', 'sut', 'banan', 'non',  
        'piyoz', 'salat','koffe', 'kalbasa', 'suv']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))        


for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
else:
          print(f"Do'konimizda {mahsulot} yo'q")

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)

users = ['alisher','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
son =float(input("Juft son kiriting: "))
if son%2:
    print("Bu son juft emas.")
else:
    print("raxmat")
yosh = int(input("Yoshigiz nechida?"))

if yosh<=4 or yosh>=60:
      narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm") 
x = float(input("Birinchi soni kiriting"))
y = float(input("Ikkinchi son kiriting"))
if x==y:
    print(f"{x}={y}")
elif x<y:
     print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

 
son = int(input("Istalgan sonni kiriting"))

for n in range(2,11):
    if not (son%n): 
     print(f"{son} soni {n} ga qoldiqsiz bolinadi")


users = ['alisher','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")
users = ['Alisher', 'aziza', "yasina", 'umar']
login = input("Yangi login tanlang!")

if login in users:
    print("Login band,yangi login tanlang")
else:
    print(f"Xush kelibsiz, {login.title()}!")

