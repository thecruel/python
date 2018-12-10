print("""
********************************
***** # KULLANICI GİRİŞİ # *****
********************************
""")

username = "kuruel"
password = "kuruel"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı: ")
    parola = input("Parola: ")

    if(username == kullanıcı_adı and password == parola):
        print("Giriş başarılı.")
        break

    elif(username == kullanıcı_adı and password != parola):
        giriş_hakkı -= 1
        print("Parola hatalı!")
        if(giriş_hakkı == 0):
            print("Giriş hakkınız bitti!")
            break
        print("Kalan giriş hakkınız: ",giriş_hakkı)

    else:
        giriş_hakkı -= 1
        print("Böyle bir kullanıcı yok!")
        if(giriş_hakkı == 0):
            print("Giriş hakkınız bitti!")
            break

        print("Kalan giriş hakkınız: ",giriş_hakkı)

    if(giriş_hakkı == 0):
        print("Giriş hakkınız bitti!")

        break