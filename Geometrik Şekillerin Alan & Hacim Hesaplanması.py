# Bu kodda nesne tabanlı programlama yardımıyla geometrik şekillerin hacim ve alanını hesaplayan bir algoritma geliştirdim.
# çeşitli modül,fonksiyon,metod ve control flow'lar kullanarak menüde belirtilen tercihlere göre kullanıcı istediği
# geometrik şeklin alanını hacmini hesaplayabilir. Girilen argümanların şeklin uygunluğu itibariyle uygun olmadığı durumlar
# olmakla beraber hesaplamalar ve çıkan sonuçlar bilimseldir.


import time
from math import *


class geometricalShapes:
    pi = 3.14

    def __init__(self, height, Sidelength):
        self.yukseklik = height
        self.Kenaruzunlugu = Sidelength
        self.dongu = True

    def Cube(self, tercih):
        if tercih == True:
            return float((self.Kenaruzunlugu) ** 3)

        elif tercih == False:
            return float(6 * (self.Kenaruzunlugu) ** 2)

    def quadrangular(self, tercih):
        kisa_kenar1 = float(input("1.kısa kenarın uzunluğu: "))
        kisa_kenar2 = float(input("2.kısa kenarın uzunluğu: "))
        uzun_kenar = float(input("uzun kenarın uzunluğu: "))

        if tercih == True:
            islem = kisa_kenar1 * (uzun_kenar) * kisa_kenar2
            return float(islem)

        elif tercih == False:
            islem_1 = uzun_kenar * kisa_kenar2 + kisa_kenar2 * kisa_kenar1 + uzun_kenar * kisa_kenar1
            islem_2 = 2 * islem_1
            return float(islem_2)

    def Sphere(self, tercih):
        yaricap = float(input("Kürenin yarıçapını giriniz: "))

        if tercih == True:
            return float((4 / 3) * (yaricap) ** 3 * self.pi)

        elif tercih == False:
            return float(4 * (self.pi) * yaricap ** 2)

    def cylinder(self, tercih):
        yaricap_1 = float(input("silindirin yarıçapını giriniz: "))
        if tercih == True:
            return float(self.pi * (yaricap_1) ** 2 * (self.yukseklik))

        elif tercih == False:
            return float(2 * self.pi * yaricap_1 * (yaricap_1 + self.yukseklik))

    def Cone(self, tercih):
        yaricap_2 = float(input("Koninin yarıçapını giriniz: "))
        if tercih == True:
            islem_3 = (1 / 3) * (self.pi) * (yaricap_2) * 2 * (self.yukseklik)
            return float(islem_3)

        elif tercih == False:
            islem_4 = self.pi * yaricap_2 * (yaricap_2 + sqrt((yaricap_2 + self.yukseklik)))
            return float(islem_4)


sekil = geometricalShapes(height=7, Sidelength=6)

print("                      MENÜ           \n\n "
      " **** GEOMETRİK ŞEKİLLERDE HACİM-ALAN HESABI *** \n\n"
      "## LÜTFEN SEÇİN\n\n"
      "Küp'ün hacmi ve alanı için 1 i seçiniz:\n"
      "\thacim için --> 1.1 yaz.\n"
      "\talan için --> 1.2 yaz.\n\n"
      "Dikdörtgenler Prizması'nın hacmi ve alanı için 2 i seçiniz:\n"
      "\thacim için --> 2.1 yaz.\n"
      "\talan için --> 2.2 yaz.\n\n"
      "Küre'nin hacmi ve alanı için 3 ü seçiniz:\n"
      "\thacim için --> 3.1 yaz.\n"
      "\talan için --> 3.2 yaz.\n\n"
      "Silindir'in hacmi ve alanı için 4 ü seçiniz:\n"
      "\thacim için --> 4.1 yaz.\n"
      "\talan için --> 4.2 yaz.\n\n"
      "Koni'nin hacmi ve alanı için 4 ü seçiniz:\n"
      "\thacim için --> 5.1 yaz.\n"
      "\talan için --> 5.2 yaz.\n\n")

while sekil.dongu:

    sekil_secim = input('İşlemini görmek istediğiniz geometrik şekli menüden seçiniz: ')
    alan_hacim_secim = input('Geometrik şeklin hacim veya Alan hesabı için gerekli numarayı menüden seçiniz: ')

    if sekil_secim == '1':
        if alan_hacim_secim == '1.1':
            print("KÜP'ün hacmi hesaplanıyor...")
            time.sleep(2)
            print(sekil.Cube(True))
            continue


        elif alan_hacim_secim == '1.2':
            print("KÜP'ün alanı hesaplanıyor...")
            time.sleep(2)
            print(sekil.Cube(False))
            continue

    elif sekil_secim == '2':
        if alan_hacim_secim == '2.1':
            print("DİKDÖRTGEN PRİZMA'nın hacmi hesaplanıyor...")
            time.sleep(2)
            print(sekil.quadrangular(True))
            continue

        elif alan_hacim_secim == '2.2':
            print("DİKDÖRTGEN PRİZMA'nın alanı hesaplanıyor...")
            time.sleep(2)
            print(sekil.quadrangular(False))
            continue

    elif sekil_secim == '3':
        if alan_hacim_secim == '3.1':
            print("KÜRE'nİn hacmi hesaplanıyor...")
            time.sleep(2)
            print(sekil.Sphere(True))
            continue


        elif alan_hacim_secim == '3.2':
            print("KÜRE'nİn alanı hesaplanıyor...")
            time.sleep(2)
            print(sekil.Sphere(False))
            continue

    elif sekil_secim == '4':
        if alan_hacim_secim == '4.1':
            print("SİLİNDİR'in hacmi hesaplanıyor...")
            time.sleep(2)
            print(sekil.cylinder(True))
            continue


        elif alan_hacim_secim == '4.2':
            print("SİLİNDİR'in alanı hesaplanıyor...")
            time.sleep(2)
            print(sekil.cylinder(False))
            continue

    elif sekil_secim == '5':
        if alan_hacim_secim == '5.1':
            print("KONİ'nin hacmi hesaplanıyor...")
            time.sleep(2)
            print(sekil.Cone(True))
            continue


        elif alan_hacim_secim == '5.2':
            print("KONİ'nin alanı hesaplanıyor...")
            time.sleep(2)
            print(sekil.Cone(False))
            break
