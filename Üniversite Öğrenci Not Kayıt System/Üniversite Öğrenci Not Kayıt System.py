# Bu kodda  üniversite öğrencisi/öğrencilerinin vize,final,quiz ve lab sınavlarından aldığı notları bir dosyaya aktararak ve bu dosyadan okunacak verilere göre dönem sonu harf notunun hesaplanmasını
# ve harf notlarını bir txt dosyasına nasıl aktaracağımızı işledik.
# Ayrıca kaydettiğimiz verileri file den nasıl sileriz bunları da kodladık.


import time

def harf_notu_hesapla(data):
    liste = data.split(':')
    ogrenciAd_Soyad = liste[0]

    notlar = liste[1].split(',')
    vize_1 = float(notlar[0])
    vize_2 = float(notlar[1])
    quiz1 =  float(notlar[2])
    quiz2 = float(notlar[3])
    final = float(notlar[4])
    lab1 =  float(notlar[5])
    lab2 = float(notlar[6])


    ortalama = float(((vize_1+vize_2)/2)*(0.30) + final*(0.50) + ((quiz1+quiz2)/2)*0.05 + ((lab1+lab2)/2)*0.15)

    if  0<=ortalama and ortalama<39.50:
        harf_notu = "FF"
    elif 39.50<=ortalama and ortalama<45:
        harf_notu = "FD"
    elif 45.00 <= ortalama and ortalama <50:
        harf_notu = "DD"
    elif 50.00 <= ortalama and ortalama < 60:
        harf_notu = "DC"
    elif 60.00 <= ortalama and ortalama < 65:
        harf_notu = "CC"
    elif 65.00 <= ortalama and ortalama < 75:
        harf_notu = "CC"
    elif 75.00 <= ortalama and ortalama < 85:
        harf_notu = "CB"
    elif 85.00 <= ortalama and ortalama < 90:
        harf_notu = "BA"
    elif 90 <= ortalama and ortalama < 100:
        harf_notu = "AA"
    else:
        print('beklenmeyen sonuç')

    return ogrenciAd_Soyad + ": " + harf_notu + "\n"  #bir sonraki öğrencinin verisi için \n kullandık


def harf_notlari_oku():

    with open("Sinav Notlari.txt","r",encoding="utf-8") as file:


        data = file.readlines()
        l = []
        for i in data:
            l.append(harf_notu_hesapla(i)[:-1])
        print(l)


def not_bilgilerini_gir():
    ad = input('Adınızı giriniz: ')
    soyad = input('Soyadınızı giriniz: ')
    vize_1 = input("1.vize notunuz : ")
    vize_2 = input("2.vize notunuz : ")
    quiz1 = input("quiz-1 notunuz : ")
    quiz2 = input("quiz-2 notunuz : ")
    final = input("final notunuz : ")
    lab1 = input("Lab-1 notunuz : ")
    lab2 = input("Lab-2 notunuz : ")

    with open("Sinav Notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+ " "+soyad+':'+vize_1+','+vize_2+','+quiz1+','+quiz2+','+final+','+lab1+','+lab2+'\n' )


def notlari_kayitet():
    with open("Sinav Notlari.txt","r",encoding="utf-8") as file:
        liste = []  #bir listeye attık çünkü her bir öğrenci not bilgisinden sonra önceki öğrecileri de listeye atar ve hepsini başka dosyaya kaydetmemiz gerekir.
        for i in file:
            liste.append(harf_notu_hesapla(i))

    with open("Öğrenci_Harf_Notu_Bilgileri.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)


def dosyadanVeri_Sil():
    silinecek_veri = int(input('Sileceğiniz verinin index numarasını giriniz: '))
    print(f"{silinecek_veri+1}.veri 2 saniye sonra siliniyor..")
    time.sleep(2)
    with open("Öğrenci_Harf_Notu_Bilgileri.txt","r",encoding="utf-8") as file_3:
        liste_1 = []
        for i in file_3:
            liste_1.append(i)


    liste_1.pop(silinecek_veri)

    with open("Öğrenci_Harf_Notu_Bilgileri.txt","w",encoding="utf-8") as file_4:
        for i in liste_1:
            file_4.write(i)


    with open("Sinav Notlari.txt","r",encoding="utf-8") as file:
        liste_2 = []
        for i in file:
            liste_2.append(i)
    liste_2.pop(silinecek_veri)
    with open("Sinav Notlari.txt", "w", encoding="utf-8") as file:
        for i in liste_2:
            file.write(i)

while True:
    islem = input("Harf Notunu Oku --> [1]\nNot Gir --> [2]\nNotları Kayıt Et --> [3]\nVeri silme --> [4]\nÇıkış Yap --> çıkış için q'ya basınız.\n"
                  ": ")

    if islem == 'q':
        print("2 saniye sonra çıkış yapılıyor.")
        time.sleep(2)
        break

    elif 0<int(islem) and int(islem)<=4:

        if int(islem) == 1:
            harf_notlari_oku()
        elif int(islem) == 2:
            not_bilgilerini_gir()
        elif int(islem) == 3:
            notlari_kayitet()
        elif int(islem) == 4:
            print("Sonuçlar dosyasından veri silme ve sınav notları dosyasını güncelleme işlemine hoş geldiniz.")
            dosyadanVeri_Sil()
            harf_notlari_oku()

    else:
        raise TypeError("Seçeneklerin dışında bir girdi girdin.")

