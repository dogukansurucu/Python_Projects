# Datetime Module & Strptime Function ile Araba Bakım Zamanı


# Bir kişinin sahip olduğu araç var ve bu aracın trafiğe çıkış tarihi kullanıcıdan bilgi olarak alınıyor.
# biz datetime modülü metodlarını kullanarak bu string ifadeyi düzenli hale getirip yıl ay gün bilgisini alarak şuanki zamandan çıkarıyoruz.
# aradaki farkı gün olarak alıyoruz. Eğer 365 günden az ise 1.yıl 365 ile 365*2 arasındaysa 2.yıl bakım zamanı gelmiştir.
# ve bu şekilde 5 bakım yılını baz aldık.



from datetime import datetime
import time

while True:
    try:
        cikis_Tarihi = input("""\nÇıkış tarihini;
gün(sayı ile) , ay(uzun hali,ingilizce) , yıl(uzun hali) biçiminde alınız.
         \n\narabanızın trafiğe çıkış tarihi:  """)

        tarih = datetime.strptime(cikis_Tarihi, "%d %B %Y")

        year = tarih.year
        month = tarih.month
        day = tarih.day
        # int tipindeler

        zaman = datetime(year, month, day)
        suan = datetime.now()
        gun = (suan - zaman).days

        if gun <= 365:
            print('Aracınızın 1.bakım yılı,',"Trafiğe çıkalı {} gün olmuş.".format(gun))
            break
        elif 365 <= gun and gun <= 365 * 2:
            print('Aracınızın 2.bakım yılı,',"Trafiğe çıkalı {} gün olmuş.".format(gun))
            break
        elif 365 * 2 <= gun and gun <= 365 * 3:
            print('Aracınızın 3.bakım yılı,',"Trafiğe çıkalı {} gün olmuş.".format(gun))
            break
        elif 365 * 3 <= gun and gun <= 365 * 4:
            print('Aracınızın 4.bakım yılı,',"Trafiğe çıkalı {} gün olmuş.".format(gun))
            break
        elif 365 * 4 <= gun and gun <= 365 * 5:
            print('Aracınızın 5.bakım yılı,',"Trafiğe çıkalı {} gün olmuş.".format(gun))
            break
        else:
            print('Arabanın en fazla 5 yıl öncesine kadar trafiğe ilk çıkışın olduğu varsayıyoruz.')
            break

    except ValueError:
        print("\nKullanıcıdan alınan tarih verisiyle datetime fonksiyonu olan strptime karakterleriyle eşleşmiyor.strptime fonksiyonunu doğru kullanınız lütfen."
              "\n5 saniye sonra tekrar deneyiniz.")
        time.sleep(5)
