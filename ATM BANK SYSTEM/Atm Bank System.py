import time
import sys
import os
import math
import random
import re


class person:
    def __init__(self,ad,soyad,TC,password,anaBakiye,yedekBakiye,toplamBorc):
        self.Ad = ad
        self.Soyad = soyad
        self.TC = TC
        self.password = password
        self.anaBakiye = anaBakiye
        self.yedekBakiye = yedekBakiye
        self.toplamBorc = toplamBorc



card = person('DOĞUKAN','SÜRÜCÜ','33133409556',2302,8500,780,1935)


class Atm:
    def __init__(self):
        self.atmAD = "YAPIKREDİ"
        self.Dongu = True


    def AtmGiris(self):
        print(f"""  
            Sevgili {card.Ad} {card.Soyad},
            {self.atmAD}'ye hoş geldiniz.
        """, "-" * 32, end="\n")

        hak = 3
        while 0<hak:
            hak-=1
            sayac = 0
            try:
                sayac+=1
                sifre = int(input('Şifrenizi giriniz: '))
                TC = input('TC numaranızı giriniz: ')
                if card.password == sifre and card.TC == TC:
                    print(
                        f"TEBRİKLERR !! {sayac}.denemenizde İŞLEMİNİZ BAŞARILI, 3 saniye sonra menüye yönlendirileceksiniz.")
                    time.sleep(3)
                    self.Program()
                    break
                elif (card.password != sifre or card.TC != TC) and hak != 0:
                    print(f"Hatalı şifre veya kimlik bilgisi girdiniz, Kalan hakkınız {hak}")
                elif hak == 0:
                    print(""" şifrenizi 3 defa hatalı girdiğinizden dolayı kartınız bloke olmuştur.
                    Lütfen en yakın şubemize başvurunuz.
                    """)
                    sys.exit()
            except ValueError:
                print("Şifreniz number değerlerden oluşmalıdır.")

    def Program(self):
        secim = self.Menu()

        if secim == 1:
            print("bakiye sorgulama seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.bakiye()
        elif secim == 2:
            print("bakiye borç sorgulama seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.BorcSorgula()
        elif secim == 3:
            print("bakiye çekme seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.Paracek()
        elif secim == 4:
            print("bakiye yatırma seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.ParaYatir()
        elif secim == 5:
            print("bakiye borç ekleme/ödeme seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.borcEklemeOdeme()
        elif secim == 6:
            self.CIKIS()

    def Menu(self):
        print(
            f"\nMerhabalar, {self.atmAD}'a hoşgeldiniz.Sayın {card.Ad} {card.Soyad}.\nLütfen aşağıdaki menüden yapmak istediğiniz işlemi seçiniz.\n\n")
        print(' \tİ\tŞ\tL\tE\tM\t\tM\tE\tN\tÜ\tS\tÜ\t '.expandtabs(2).center(55, '*').rjust(60))
        print("""
                     [1] Bakiye Sorgulama
                     [2] Borç Sorgulama
                     [3] Para Çekme
                     [4] Para Yatırma
                     [5] Borç Ödeme/Ekleme
                     [6] Kart İade
             """)

        secim = int(input("Seçiminiz: "))

        while secim < 1 or secim > 6:
            secim = int(input("\nLütfen 1 ve 5 arasında geçerli bir değer giriniz.\n:"))

        return secim

    def bakiye(self):
        """
        with open("Atm Bakiye Sorgulama.txt","r",encoding="utf-8") as file:
        """

        if os.path.exists("Atm Bakiye Sorgulama.txt") == True:
            with open("Atm Bakiye Sorgulama.txt", "r", encoding="utf-8") as file:
                print("Toplam Bakiyeniz: {} TL'dir.".format(file.read()))
        else:
            toplamBakiye = card.anaBakiye + card.yedekBakiye
            with open("Atm Bakiye Sorgulama.txt", "w", encoding="utf-8") as file:
                file.write(str(toplamBakiye))
            with open("Atm Bakiye Sorgulama.txt", "r", encoding="utf-8") as file:
                print("Toplam Bakiyeniz: {} TL'dir.".format(file.read()))

        self.Dongu = False
        self.MENUDON()

    def BorcSorgula(self):

        try:
            with open("Atm borç sorgulama.txt","r",encoding="utf-8") as file:
                borc = file.read()

            if int(borc) > 0:
                secenek = input(""" {} TL BORCUNUZ BULUNMAKTADIR.
                                 ÖDEMEK İÇİN --> [1]
                                 BORÇ EKLEMEK İÇİN --> [2]
                                 MENÜYE DÖNMEK YA DA ÇIKIŞ YAPMAK İÇİN --> [3]
                                 'yi tuşlayınız.
                                  : """.format(borc))

                while secenek != "1" and secenek != "2" and secenek!="3":
                    secenek = input(""" {} TL BORCUNUZ BULUNMAKTADIR.
                                                     ÖDEMEK İÇİN --> [1]
                                                     BORÇ EKLEMEK İÇİN --> [2]
                                                     MENÜYE DÖNMEK YA DA ÇIKIŞ YAPMAK İÇİN --> [3]
                                                     'yi tuşlayınız.
                                                      : """.format(borc))

                if secenek == "1":
                    self.ParaYatir()

                elif secenek == "2":
                    self.borcEklemeOdeme(3)
                    self.Dongu = False
                    self.MENUDON()
                elif secenek == "3":
                    self.Dongu = False
                    self.MENUDON()

            elif int(borc) <= 0:
                secenek = input("""BORCUNUZ BULUNMAMAKTADIR.AKSİNE {} TL kardasınız.
                                                 BORÇ EKLEMEK İÇİN --> [1]
                                                 MENÜYE DÖNMEK YA DA ÇIKIŞ YAPMAK İÇİN --> [2]
                                                 'yi tuşlayınız.
                                                  : """.format(math.fabs(int(borc))))

                while secenek != "1" and secenek != "2":
                    secenek = input("""BORCUNUZ BULUNMAMAKTADIR.AKSİNE {} TL kardasınız.
                                                                     BORÇ EKLEMEK İÇİN --> [1]
                                                                     MENÜYE DÖNMEK YA DA ÇIKIŞ YAPMAK İÇİN --> [2]
                                                                     'yi tuşlayınız.
                                                                      : """.format(math.fabs(int(borc))))
                if secenek == "1":
                    self.borcEklemeOdeme(3)
                    self.Dongu = False
                    self.MENUDON()
                elif secenek == "2":
                    self.Dongu = False
                    self.MENUDON()
                else:
                    print("1 ve 2 dışında bir seçenek seçtiniz.")
                    self.Dongu = False
                    self.MENUDON()


        except FileNotFoundError:
            with open("Atm borç sorgulama.txt","w",encoding="utf-8") as file:
                file.write(str(card.toplamBorc))

            with open("Atm borç sorgulama.txt", "r", encoding="utf-8") as file:
                print("Toplam Borcunuz: {} TL'dir.".format(file.read()))

            self.Dongu = False
            self.MENUDON()


    def Paracek(self):

        """
        para kaldı mı kalmadı mı onları sorgulayan kalmadıysa para aktarına yönlendirme gibi bir kod bloğu

        """

        CekilenBakiye = int(input("Lütfen çekeceğiniz miktarı giriniz: "))

        with open("Atm Bakiye Sorgulama.txt", "r", encoding="utf-8") as file:

            cekilenPara = int(file.read())-CekilenBakiye


        with open("Atm Bakiye Sorgulama.txt", "w", encoding="utf-8") as file:
            file.write(str(cekilenPara))

        self.Dongu = False
        self.MENUDON()

    def ParaYatir(self):
        yatirilacak_yer = input("""
        [1]-- Ana bakiye'ye para yatırma
        [2]-- Borç Ödemek için para yatırma
        : """)

        while True:
            try:
                assert (yatirilacak_yer == "1" or yatirilacak_yer == "2"), "Her şey yolunda"

                if yatirilacak_yer == "1":
                    YatirilacakBakiye = int(input("Lütfen aktaracağınız miktarı giriniz: "))

                    with open("Atm Bakiye Sorgulama.txt", "r", encoding="utf-8") as file:
                        bakiye = file.read()

                    yeni_bakiye = YatirilacakBakiye + int(bakiye)

                    with open("Atm Bakiye Sorgulama.txt", "w", encoding="utf-8") as file:
                        file.write(str(yeni_bakiye))


                elif yatirilacak_yer == "2":
                    self.borcEklemeOdeme(2)
                    self.Dongu = False
                    self.MENUDON()
            except:
                yatirilacak_yer = input("yatırılacak yer para: [1/2]: ")

            self.Dongu = False
            self.MENUDON()

    def borcEklemeOdeme(self,a=1):
        if a == 3:
            borclanacakMIKTAR = int(input("Ne kadar Borç Eklemek istiyorsunuz: "))
            with open("Atm borç sorgulama.txt","r",encoding="utf-8") as file:
                borc = file.read()
            toplamBORC =int(borc)+borclanacakMIKTAR
            with open("Atm borç sorgulama.txt","w",encoding="utf-8") as file:
                file.write(str(toplamBORC))

        elif a == 2:
            odenecekMIKTAR = int(input("Ne kadar Borç Ödemek istiyorsunuz: "))

            with open("Atm borç sorgulama.txt", "r", encoding="utf-8") as file:
                mevcut_borc = int(file.read())
            guncel_borc = mevcut_borc-odenecekMIKTAR
            with open("Atm borç sorgulama.txt", "w", encoding="utf-8") as file:
                file.write(str(guncel_borc))

        elif a == 1:
            print("""
            BU BİR BİLGİLENDİRME YAZISIDIR !!!
            MENÜDEN,
            ---- ÖDEMEK YAPMAK İÇİN PARA YATIR SEÇENEĞİNİ SEÇİNİZ.
            ---- BORÇ EKLEMEK İÇİN BORÇ SORGULAMA SEÇENEĞİNİ SEÇİNİZ.
            
            *** 5 SANİYE SONRA YÖNLENDİRİLİYORSUNUZ. ***
            """)
            time.sleep(5)
            self.Dongu=False
            self.MENUDON()

    def CIKIS(self):
        print("Bankamızı tercih ettiğiniz için teşekkür eder, İyi günler dileriz...")
        self.Dongu = False
        sys.exit()

    def MENUDON(self):
        hak = 2
        while hak > 0:
            hak -= 1

            x = int(
                input("""\nAna menüye dönmek için lütfen 7 tuşuna basınız. Kart iade için 5'e basınız\nSeçimniz: """))

            if x == 7:
                self.Program()
                break
            elif x == 5:
                self.CIKIS()
                break
            else:
                print("Yanlış tuşa bastınız.Sadece 2 tuşa basabilirsiniz !!!\n")

            if hak == 0:
                print("Hakkınız bitti.")
                exit()


banka = Atm()

banka.AtmGiris()



while banka.Dongu:
    banka.Program()





















