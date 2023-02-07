def greet(name):
    print("Hello", name)
    print("How do you do")
    greet("Sardor")


def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)


number1 = 5.4
number2 = 6.5
add_numbers(number1, number2)


def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks


marks = [55, 90, 60, 40, 30, 85]
average_marks = find_average_marks(marks)
print("Your average marks is", average_marks)
length = len(marks)
print("Length is", length)
marks_sum = sum(marks)
print("The total marks you got is", marks_sum)


def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [55, 90, 60, 40, 30, 85]
average_marks = find_average_marks(marks)
print("Your average marks is:", average_marks)

grade = compute_grade(average_marks)
print("Your grade is", grade)


def salom_ber(ism):
    print("Hello " + ism + "!")


salom_ber("Muhammadaziz")


def son(n1, n2):
    print(n1 + n2)


son(20, 35)


def bahola(ismlar):
    baholar = {}
    if ismlar:
        ism = ismlar
        baholar = input(f"ismlar {ism.title()}: ")
    return baholar


talabalar = ['elmurod', 'sardor', 'ali', 'nodir']
print(talabalar)


def avto(moshinalar):
    narxlar = {}
    while moshinalar:
        moshina = moshinalar.pop()
        moshina = input(f"avto {moshina.title()}ning narxni kiriting: ")
        narxlar[moshina] = [moshina]
    return narxlar


moshinalar = ['malibu', 'kaptiva', 'bmw', 'gentra']
narxlar = avto(moshinalar)
print(moshinalar)
print(narxlar)


def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
        return matnlar


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
katta_harf(ismlar)
print(ismlar)


def multiply(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))


def talaba_info(ism, familiya, **kwargs):
    kwargs['ism'] = ism
    kwargs['familiya'] = familiya
    return kwargs
