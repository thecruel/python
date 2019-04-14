def toplama(a,b):
    return a+b

def çıkarma(a,b):
    return a-b

def çarpma(a,b):
    return a*b

def bölme(a,b):
    return a/b

print("***İşlem Seç***")
print("1 --> Toplama")
print("2 --> Çıkarma")
print("3 --> Çarpma")
print("4 --> Bölme\n")

secim = input('Seçim: ')

sayı1 = int(input("1. Sayı: "))
sayı2 = int(input("2. Sayı: "))

if secim == '1':
    print(sayı1, "+", sayı2, "=", toplama(sayı1,sayı2))

elif secim == '2':
    print(sayı1, "-", sayı2, "=", çıkarma(sayı1,sayı2))

elif secim == '3':
    print(sayı1, "*", sayı2, "=", çarpma(sayı1,sayı2))

elif secim == '4':
    print(sayı1, "/", sayı2, "=", bölme(sayı1,sayı2))

else:
    print("Lütfen işlemi doğru seçiniz")
