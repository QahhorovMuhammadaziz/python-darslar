son = 1
while son <= 5:
    print(son, end=' ')
    son += 1

print("Kiritilgan sonning kvadiratga qaytaruvchi dastur. ")
savol = "Istalgan son kiriting"
savol += "(Dasturni toxtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print('Dastur tugadi')
        print(float(qiymat)**2)

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:

    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
        print('Dastur to\'xtadi')

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)
print('Dastur tugadi')

sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")


son = 0
while son < 10:
    son += 1
    if son % 2 == 0:
        continue
    else:
        print(son)
savol = "sevgan kitobigizni kiriting"
savol += "(barcha kitoblarni kiritib \nbolgach 'exit' deb yozing): "


while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
    print('raxmat')
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

son = 0
while son < 10:
    if son % 2 != 0:
        continue
    else:
        print(son)
