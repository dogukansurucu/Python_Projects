# Bu projemde Kapsamlı Bilimsel Hesap Makinesi yaptım.

"""
Yaptığım uygulamada toplama,çıkarma,çarpma,bölme,üs alma,karekök,ebob-ekok,log,ln,faktöriyel,mutlak değer,
sin,cos,radian gibi matematiksel işlemler yapabiliyoruz.

klavyeden girilen int float değerlere göre bir işlem yapma olayını gerçekleştireceğiz.

bir işlemdeyken başka işleme geçme olayını class yapısı ve aktif olup pasif olma durumununa göre tüm işlemlerden birine geçiş
olayını gerçekleştireceğiz.

"""

import sys
import math
import time

def menu():
    secenek = input("""
              [GELİŞMİŞ HESAP MAKİNESİ PROGRAMI]
                              ↓       
      ********************************************************
      *          |--------------------------|                *
      *          |  LÜTFEN İŞLEM SEÇİN      |\t             *
      *          |--------------------------|                *
      *      \t\t1. İşlem = Toplama                       *
      *      \t\t2. İşlem = Çıkarma                       *
      *      \t\t3. İşlem = Çarpma                        *
      *      \t\t4. İşlem = Bölme                         *
      *      \t\t5. İşlem = Üs Alma                       * 
      *      \t\t6. İşlem = Karekök                       *
      *      \t\t7. İşlem = logaritma                     *
      *      \t\t8. İşlem = Dereceyi radyana çevirme      *
      *      \t\t9. İşlem = Radyanı dereceye çevirme      *
      *      \t\t10. İşlem = Hipotenüs                    *
      *      \t\t11. İşlem = Faktöriyel                   *
      *      \t\t12. İşlem = Mutlak değer                 *
      *      \t\t13. İşlem = Ebob                         *
      *      \t\t14. işlem = Sinüs                        *
      *      \t\t15. İşlem = Cosinüs                      *
      *      \t\t16. İşlem = Çıkmak için q ya basın..."   *
      ********************************************************\n\n: """)
    return secenek

def topla(a,b):
    sonuc = a+b
    return sonuc

def cikar(a,b):
    sonuc = a-b
    return sonuc

def carp(a,b):
    sonuc = a*b
    return sonuc

def bol(a,b):
    sonuc = a/b
    return sonuc

def us_alma():
    x = int(input("üssü alınacak sayı: "))
    y = int(input("kaçıncı kuvveti alınsın:"))
    sonuc = math.pow(x,y)
    print(f"{x}**{y} isleminin sonucu: {sonuc}")

def karekok():
    hak = 2
    i = 0
    print("Unutmayın 3 hakkınız var.")
    time.sleep(3)

    while i<hak:
        z = float(input("karekökü alınacak sayı:"))
        try:
            sonuc = math.sqrt(z)
            print(f" √¯{z}  isleminin sonucu: {sonuc}")
            break
        except ValueError as e:
            print(f"Reel sayılarda, karekök kuralı gereği {z} değeri x>=0 olmalıdır.",e)

        i+=1
    else:
        z = float(input("\nSadece karmaşık sayılarfa karekök içi negatif olabilir.\nNegatif sayı giriniz: "))
        sonuc = z**(1/2)
        print("işlemin sonucu: ",sonuc," ve bir complex sayıdır.")


def log():
    x = float(input("logaritması alınacak sayı: "))
    try:
        sonuc = math.log10(x)
        print(f" log{x}  isleminin sonucu: {sonuc}")
    except ValueError:
        print(f"logaritma kurallarına göre {x} 0 dan büyük olmalı.")
    finally:
        print("İşlem başarıyla sonuçlandı.")

def radian():
    a = float(input("radyana çevrilecek dereceyi giriniz: "))
    sonuc = math.radians(a)
    print(f" {a} derecesinin radyan karşılığı: {sonuc}")


def derece():
    b = float(input("dereceye çevrilecek radyanı giriniz: "))
    sonuc = math.degrees(b)
    print(f" {b} radyanının derece karşılığı: {sonuc}")


def hipotenus():
    k = float(input("dik kenar uzunluğu: "))
    l = float(input("taban uzunluk: "))
    sonuc = math.sqrt(math.pow(k,2) + math.pow(l,2))
    print(f" kenarları {k} ve {l} metre uzunluktaki bir üçgenin hipotenüsü: {sonuc}")

def faktoriyel():
    m = int(input("faktöriyeli alınacak sayı: "))
    try:
        sonuc = math.factorial(m)
        print(f" {m} sayısının faktöriyeili: {sonuc}")
    except ValueError as x:
        print("Negatif sayıların faktöriyeli alınmaz\nERROR:",x)


def mutlakDeger():
    sayi = float(input("mutlak değeri alınacak sayıyı giriniz: "))
    sonuc = math.fabs(sayi)
    print(f"{sayi} sayısının mutlak değeri: {sonuc}")

def Ebob():
    a = int(input("1. sayı: "))
    b = int(input("2. sayı: "))
    sonuc = math.gcd(a,b)
    print(f"{a} ve {b} sayılarının ebobu {sonuc}")

def sin():
    islem = input(" 1- radyan cinsinden sayının sinüs değerini hesapla.\n"
                  " 2- derece cinsinden sayının sinüs değerini hesapla\n:  ")
    if  islem=="1":
        a = float(input("sinüsü alınacak radyanı giriniz: "))
        sonuc = math.sin(a)                   # radyan cinsinden a sayısının sinüs değerini hesaplar.
        print(f"{a} radyanın sinüs değeri: {sonuc}")
    elif islem=="2":
        b = float(input("sinüsü alınacak dereceyi giriniz: "))
        sonuc = math.sin(math.radians(b))     # b derecenin sinüs değerini hesaplar.
        print(f"{b} derecenin sinüs değeri: {sonuc}")

def cos():
    islem = input(" 1- radyan cinsinden sayının cosinüs değerini hesapla.\n"
                  " 2- derece cinsinden sayının cosinüs değerini hesapla\n:  ")
    if islem == "1":
        a = float(input("cosinüsü alınacak radyanı giriniz: "))
        sonuc = math.cos(a)  # radyan cinsinden a sayısının cosinüs değerini hesaplar.
        print(f"{a} radyanın cosinüs değeri: {sonuc}")
    elif islem == "2":
        b = float(input("cosinüsü alınacak dereceyi giriniz: "))
        sonuc = math.cos(math.radians(b))  # a derecenin cosinüs değerini hesaplar.
        print(f"{b} derecenin cosinüs değeri: {sonuc}")



while True:
    print("\nYapmak istediğiniz işlemi seçiniz.")
    tercih = menu()


    if tercih == "q":
        sys.exit()


    elif tercih=="1":
        a = float(input("1.sayi: "))
        b = float(input("2.sayi: "))

        print("işleminiz 5 saniye sonra gerçekleşiyor.")
        time.sleep(5)
        print(f"{a} + {b} = {topla(a,b)}")
        time.sleep(3)

    elif tercih=="2":
        a = float(input("1.sayi: "))
        b = float(input("2.sayi: "))

        print("işleminiz 5 saniye sonra gerçekleşiyor.")
        time.sleep(5)
        print(f"{a} - {b} = {cikar(a,b)}")
        time.sleep(3)

    elif tercih=="3":
        a = float(input("1.sayi: "))
        b = float(input("2.sayi: "))

        print("işleminiz 5 saniye sonra gerçekleşiyor.")
        time.sleep(5)
        print(f"{a} x {b} = {carp(a,b)}")
        time.sleep(3)

    elif tercih=="4":
        a = float(input("1.sayi: "))
        b = float(input("2.sayi: "))

        print("işleminiz 5 saniye sonra gerçekleşiyor.")
        time.sleep(5)
        print(f"{a} / {b} = {bol(a,b)}")
        time.sleep(3)


    elif tercih == "5":
        us_alma()
        time.sleep(3)

    elif tercih == "6":
        karekok()
        time.sleep(3)
    elif tercih == "7":
        log()
        time.sleep(3)

    elif tercih == "8":
        radian()
        time.sleep(3)

    elif tercih== "9":
        derece()
        time.sleep(3)

    elif tercih == "10":
        hipotenus()
        time.sleep(3)

    elif tercih == "11":
        faktoriyel()
        time.sleep(3)

    elif tercih == "12":
        mutlakDeger()
        time.sleep(3)

    elif tercih == "13":
        Ebob()
        time.sleep(3)

    elif tercih == "14":
        sin()
        time.sleep(3)

    elif tercih == "15":
        cos()
        time.sleep(3)


    else:
        raise Exception("Menü dışında bir kullanıcı bilgisi algılandı.")







