import random

sayı1 = int(input("Parola minimum kaç karakter olsun?: "))
sayı2 = int(input("Parola minimum kaç karakter olsun?: "))
uzunluk = random.randint(sayı1,sayı2)

harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "0123456789"
karakterler = "\"'!#@.,$"

while True:
    giriş_sayı = input("Parolanızda sayı olsun mu? [E/H]: ")
    if giriş_sayı != 'E' and giriş_sayı != 'H':
        print("Hatalı giriş yaptınız. Lütfen E veya H girin\n")
        continue

    while True:
        giriş_harf = input("Parolanızda harf olsun mu? [E/H]: ")
        if giriş_harf != 'E' and giriş_harf != 'H':
            print("Hatalı giriş yaptınız. Lütfen E veya H girin\n")
            continue

        while True:
            giriş_karakter = input("Parolanızda özel karakter olsun mu? [E/H]: ")
            if giriş_karakter != 'E' and giriş_karakter != 'H':
                print("Hatalı giriş yaptınız. Lütfen E veya H girin\n")
                continue
            break
        break
    break


if giriş_sayı == 'E' and giriş_harf == 'E' and giriş_karakter == 'E':
    list = karakterler + sayilar + harfler

elif giriş_sayı == 'E' and giriş_harf == 'E' and giriş_karakter == 'H':
    list = sayilar + harfler

elif giriş_sayı == 'E' and giriş_harf == 'H' and giriş_karakter == 'E':
    list = karakterler + sayilar

elif giriş_sayı == 'H' and giriş_harf == 'E' and giriş_karakter == 'E':
    list = karakterler + harfler

elif giriş_sayı == 'H' and giriş_harf == 'H' and giriş_karakter == 'E':
    list = karakterler

elif giriş_sayı == 'H' and giriş_harf == 'E' and giriş_karakter == 'H':
    list = harfler

elif giriş_sayı == 'E' and giriş_harf == 'H' and giriş_karakter == 'H':
    list = sayilar

password = ''

for a in range(uzunluk):
    password += random.choice(list)

print(password)

