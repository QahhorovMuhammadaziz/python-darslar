fruits = ['apple',  'peach', 'fig',  "apricot"]
values = [12000, 18000, 10900, 22000, 25]
print(fruits[0].title())
print(fruits[1].title())
print(fruits[2].title())
print(fruits[3].title())
values.remove(25)
print(values)

values.remove(10900)
print(values)

ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

names = ['Ali', 'Vali', 'Hasab', 'Husan', "G'ani"]
print("Hello " + names[0] + " How are you doing?")
print(f"{names[2]} va {names [3]} twins")
print(names[-1] + "He spun the wheel")

velues = [30, 45, 66, -25, 70, 110, 280,]
velues.remove(-25)
print(velues)
velues.append(-35)
print(velues)

friends = ['Elmurod',  'Sardor', 'Nodir', 'Ozod']
prices = [12000, 18000, 30000, 45000]
shopping = ["meat", "fat", "potatoes", "onion", 'banana']
product = shopping.pop(3)
print("I " + product + " buy ")
print("product not received; ", shopping)
cars = []
cars.append("Nexia")
cars.append("Malibu")
cars.append("Lasseti")
cars.append("Cobilt")
cars.append("Nexia")
cars.remove("Nexia")
print(cars)
print(cars)
del cars[1]
# print(cars)
cars.insert(0, "Malibu")
print(cars)
print(friends)
print(friends[2].upper())
print(friends[0].title())
print(prices[0] + prices[1])
friends[0] = 'jamshid'
print(friends)
friends[0] = 'Elmurod'
print(friends)
friends.append('Muzaffar')
print(friends)
friends.insert(1, 'shoxruh')
print(friends)

friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

ismlar = ['Elmurod', 'Sardor', "nodir"]
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[1]} va {ismlar[2]} do'stlar")
print(ismlar[-1] + " Moshina mindi")
sonlar = [18, 25, 38, 1988, 20200, -90, 110, -44, 33_800_44_22, 112.4]
print(sonlar)
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[2] = sonlar[4] + 48
del sonlar[4]
print(sonlar)


t_shaxslar = []
t_shaxslar = ['Saror', 'Jamshid', 'Nodir', 'Umid', 'Elmurod']
print(f"\nMen ortoglarimni {t_shaxslar.pop(1)} bilan,\n\
    suhbat qilisni istardim\n")

friends = []
friends.append('Elmurod')
friends.append('Jamshid')
friends.append('Nodir')
friends.append('Sardor')
friends.append('Qilichbek')
print(friends)
friends.remove('Nodir')
friends.remove('Qilichbek')
print(friends)
friends.append('ozod')
friends.insert(0, 'shoxrux')
friends.insert(3, 'muhammadqodir')
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
print("\nKeling mehmonlar:", mehmonlar)
