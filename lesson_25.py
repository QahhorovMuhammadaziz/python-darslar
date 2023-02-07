def solish_tir(a, b):
    if a > b:
        print(f"{a} soni {b} dan katta")
    else:
        print(f"{a} soni {b} dan kichik")


def toliq_ism(ism, familiya):
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")


def yosh_hisobla(ism, tugilgan_yil):
    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")


def yoshni_sora(yosh):
    if yosh <= 80:
        print('Siz pensiya yoshidasiz!')
    else:
        print('Bu soni kiritish mumkun emas')


yoshni_sora(yosh=70)
