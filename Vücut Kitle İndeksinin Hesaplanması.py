
# Bu kodu kısaca özetleyecek olursak bir kişinin vücut kitle indeksini hesaplayarak kilo durumunu(zayıf,normal,fazla kilolu vs.)
# ölçmüş oluyoruz.Bunun için gerekli argümanlar kullanıcıdan alacağımız kişinin vücut ağırlı(kg) ve boy uzunluğu(m) olacak.
# tabi öncelikle program başlangıcında bizden bir input değeri isteniyor ve ben bunun için 1 değeri girilirse vücut indeks hesaplanan kod bloğu çalıştırılır.Eğer 0 değeri girilirse programdan çıkılır
# Ancak string bir değer girilirse menü işlemelere girmeden string hata mesajı yollar bunun yanısıra 0 ve 1 dışında number bir ifade girilirse Raise ile hata mesajı oluşturduk.


import time
import sys

print(""" \nHAP BİLGİ !!! Vücut kitle indeksi, vücut ağırlığının boy uzunluğunun karesine bölünmesiyle (kg/m²) hesaplanır.
     \t\t  Lütfen sırasıyla Kilonuzu(kg),Boyunuzu(cm) giriniz.\n""")

while True:

    try:
        secim = int(input("Vücut Kitle indeksinizi hesaplamak için 1,"
                          "Çıkış yapmak için 0 ı tuşlayın.\n: "))
        if secim == 1:

            kisi_Ad = input("Adınız nedir : ")
            kilo = float(input("kilonuzu kg cinsinden giriniz : "))
            boy_cm = float(input("Boyunuzu cm cinsinden giriniz : "))

            metre = 0.01

            try:
                kilo_index = (kilo) / (boy_cm * metre) ** 2

                zayif = (0 <= kilo_index < 18.5)
                normal = (18.5 <= kilo_index and kilo_index < 25)
                fazla_Kilolu = (25 <= kilo_index and kilo_index < 30)
                obez = (30 <= kilo_index and kilo_index < 40)
                morbidObez = kilo_index >= 40

                if zayif:
                    print(f" {kisi_Ad} bey kilo indeksiniz : {kilo_index} , değerlendirmelere göre İdeal kilonun altındasınız.")
                    break
                elif normal:
                    print(f" {kisi_Ad } bey kilo indeksiniz : {kilo_index} , değerlendirmelere göre İdeal kilodasınız.")
                    break
                elif fazla_Kilolu:
                    print(f" {kisi_Ad } bey kilo indeksiniz : {kilo_index} , değerlendirmelere göre İdeal kilonun üstündesiniz(fazla kilolu). ")
                    break
                elif obez:
                    print(f" {kisi_Ad } bey kilo indeksiniz : {kilo_index} , değerlendirmelere göre İdeal kilonun çok üstünde (obez) ")
                    break
                elif morbidObez:
                    print(f" {kisi_Ad } bey kilo indeksiniz : {kilo_index} , değerlendirmelere göre İdeal kilonun çok üstünde (morbid obez) ")
                    break
                else:
                    print("Koşullar dışında bir sonuçla karşılaştık.5 saniye sonra tekrar seçime yönlendiriliyorsunuz.")
                    time.sleep(5)

            except ZeroDivisionError:
                print("Payda 0 olamaz.")

        elif secim == 0:
            print("3 saniye sonra çıkış yapmış olacaksınız...")
            time.sleep(3)
            sys.exit()

        else:
            raise TypeError("1 ve 0 dışında bir sayı girdiniz.Lütfen 1 ve 0 dışında değer girmeyiniz.")

    except ValueError:
        print("BAŞARISIZ !!! String bir ifade girdiniz.Number ifade girmek için 2 saniye sonra tekrar deneyiniz.")
        time.sleep(2)
