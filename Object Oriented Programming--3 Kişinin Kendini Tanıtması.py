# 3 kişinin ismini,yaşını,eğitim bilgisini,mesleğini,hobilerini ve maaşını yazdıran bir kod
# aslında bu koddaki amacım 3 kişinin hayatını kısaca anlatmakdan ziyade bu işlevleri
# yerine getirirken nesne tabanlı programlamanın önemini,metodlarını,fonksiyonlarını
# nesne tabanlı programlamada nesneler üzerinden nasıl işlem yapıldığını kavramak amacıyla
# pratik yaptım.

import time

class UserPerson:


    def __init__(self,name,year,gmail,job,education_Status,Maas=0):
        self.ad_Soyad = name
        self.yearofbirthday = year
        self.mail_Adress = gmail
        self.Is = job
        self.egitim_durumu = education_Status
        self.maas = Maas

    def Yas(self):
        return 2022-self.yearofbirthday

    def Hobi(self,oyun,muzik,gezme):
        if self.Is == 'Computer Engineering':
            return oyun
        elif self.Is == 'Aktrist':
            return muzik
        elif self.Is == 'CEO':
            return gezme

    def languenge(self,yabanci_dil):
        return yabanci_dil


p1 = UserPerson(name='Doğukan Sürücü',year=2001,gmail='surucudogukan3@gmail.com',job='Computer Engineering',education_Status='Üniversite')
p2 = UserPerson(name='Hakan Temelli',year=1995,gmail='hkn_tmlli7@gmail.com',job='Aktrist',education_Status='Üniversite_Mezunu',Maas=11000)
p3 = UserPerson(name='Ali Serdengeçti',year=1985,gmail='srdn_ali1@gmail.com',job='CEO',education_Status='Üniversite_Mezunu',Maas=35000)


kisisayisi=3
print("max 3 person bilgisi alabilirsiniz.Person bilgilerini almak için 1-3 arasında bir seçim yapınız.\nSeçenekler dışında bir numara girerseniz person bilgisi alınmaz ve hakkınız boşa gider.\n10 SANİYE SONRA SEÇİM YAPINIZ.")
time.sleep(10)

while kisisayisi>0:
    print(f"{kisisayisi} hakkınız kaldı.")
    kisisayisi-=1
    sayi = int(input('Kullanıcı numarasını giriniz: '))

    if sayi == 1:
        print(f"Merhaba! Benim adım {p1.ad_Soyad} , {p1.Yas()} yaşındayım. İstanbul Gelişim {p1.egitim_durumu}'sinde {p1.Is} 3.sınıf öğrencisiyim."
              f"\nB1 seviyesinde {p1.languenge('English')} biliyorum. Hobim {p1.Hobi(oyun='Counter Strike', muzik='Gitar', gezme='Balık')} oynamaktır."
              f"\nÖğrenci olduğum için gelirim {p1.maas}.Benimle iletişime geçmek için {p1.mail_Adress}'e mail atabilirsiniz.")

    elif sayi == 2:
        print(f"Merhaba! Benim adım {p2.ad_Soyad} , {p2.Yas()} yaşındayım. {p2.egitim_durumu} biriyim ve {p2.Is}'im."
              f"\nAylık gelirim {p2.maas}.B2 seviyesinde{p2.languenge('Spanish')} biliyorum. "
              f"Haftanın 4 günü {p2.Hobi(oyun='Counter Strike', muzik='Gitar', gezme='Balık')} çalarım.\nBenimle iletişime geçmek için {p2.mail_Adress}'e mail atabilirsiniz.")

    elif sayi == 3:
        print(f"Merhaba! Benim adım {p3.ad_Soyad} , {p3.Yas()} yaşındayım. {p3.egitim_durumu} biriyim şuan bir şirkette {p3.Is}'yum."
              f"Maaşım {p3.maas} dır.\nAkıcı bir şekilde {p3.languenge('English')} ve {p3.languenge('Spanish')} konuşabiliyorum."
              f"Haftasonları {p3.Hobi(oyun='Counter Strike', muzik='Gitar', gezme='Balık')} tutarım.\nBenimle iletişime geçmek için {p3.mail_Adress}'e mail atabilirsiniz.")

    else:
        print('Böyle bir kullanıcı numarası yoktur.')