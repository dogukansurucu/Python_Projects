# aşağıdaki kodu araştırma yaparken yabancı bir kaynakta görmüştüm. Gelin Alttaki sınıf üstteki sınıfı nasıl ezemiyor onu görelim.
# ezmekten kastım Overriding (Geçersiz Kılma) yöntemini nasıl ortadan kaldırırız ?
# Overriding'de olay alttaki sınıfın üstteki sınıfı geçersiz kılmasıydı.
# Peki bunu nasıl aşarız ? Yani üstteki sınıfın alttaki class tarafından geçersiz kılınmaması için ne gibi yöntemlere başvurmalıyız ?
# Tam burada super().__init__  veya (class adı).__init__ metodları devreye giriyor.
# Eğer üst sınıfın classı çağrılıp devamında alttaki classın çağrıldığı durumda alt sınıfta da A classın özellikleri taşınsın istiyorsak
# az önce bahsettiğim iki metotdan birini kullanmamız lazım.
# (class adı).__init__ metoduyla üstteki classı çağırıp (tabi çağırmakla bitmiyor. varsa parametreleri de unutmamak lazım) ----> (class adı).__init__(self,....)
# böylelikle overriding olayını çözmüş oluruz.


class Okul:
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        print("Okul sınıfı çalıştı.")

    def info(self):
        print("{} {} {} yaşında bir okul üyesidir.".format(self.isim, self.soyisim, self.yas))


class Ogretmen(Okul):
    def __init__(self, isim, soyisim, yas, maas, uzmanlik):
        Okul.__init__(self,isim, soyisim, yas)
        self.maas = maas
        self.uzmanlik = uzmanlik
        print("Öğretmen sınıfı çalıştı.")

    def info(self):
        print("{} {} {} yaşnda ve {} maaşı olan {} öğretmendir.".format(self.isim, self.soyisim, self.yas, self.maas,self.uzmanlik))


oh = Okul("Doğukan", "Sürücü", 34)
no = Ogretmen("Batuhan", "Sürücü", 27, 4000, "Matematik")

oh.info()
no.info()