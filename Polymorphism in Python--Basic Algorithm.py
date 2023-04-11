# Konuyu derinlemesine öğrenirken alıştırmalar yaparken çok biçimliliği özetleyecek bir kod gördüm hadi gelin birlikte ele alalım.
# Farklı sınıfların aynı isimde metoda sahip olup farklı işlem ve sonuçlar elde etmesine polimorfizm adı verilir
# yani bir sınıfta tanımladığım metodu başka classlarda farklı işlemlerde kullanıp farklı çıktılar almış oluruz.
# Buna da çok biçimlilik adını veriyoruz.

class Meslek:

    def zam(self):
        zam_oran = 0.1
        hesap = 100 + 100 * zam_oran
        print("Çalışan: ", hesap, "TL")


class Doktor(Meslek):

    def zam(self):
        zam_oran = 0.2
        hesap = 100 + 100 * zam_oran
        print("Doktor: ", hesap, "TL")


class Yazilimci(Meslek):

    def zam(self):
        zam_oran = 0.3
        hesap = 100 + 100 * zam_oran
        print("Yazılımcı: ", hesap, "TL")


meslek = Meslek()

doktor_zam = Doktor()

yazilimci = Yazilimci()

calisan = [doktor_zam, yazilimci]

for kisi in calisan:
    kisi.zam()