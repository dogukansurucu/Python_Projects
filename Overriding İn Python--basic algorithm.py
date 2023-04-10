# Overriding(geçersiz kılma) kavramı ve bir örneği
# A ve B isimli iki class düşünelim. Bu classların metodları aynı olduğunu varsayalım.
# A classını B isimli classın parametresinin içine miras bıraktığımızı düşünelim --> class B(A) .
# şimdi A classını çağırdığımızda class içerisindeki metodlar özellikler olduğu gibi çalışır.
# Daha sonra B classınız çağırdımızda normal şartlarda B classın içindeki metodların dışında miras bıraktığımız için
# A classının da özelliklerini alması gerekir ama tam burada OVERRİDİNG oluyor.Alttaki constructor ve metodlar üstteki construcrtor
# ve yapıdan daha üstün konumda oluyor ve geçersiz kılıyor.Sonuç olarak A classını B ye miras bırakmamıza rağmen A ve B classları sadece kendi
# classlarındaki yapı ve metodları çalıştırabiliyor.

class Python:
    def __init__(self, programming, name, surname):
        self.programming = programming
        self.name = name
        self.surname = surname
        print("Python")

    def info(self):
        print("{} dilini , ünlü hollandalı bilgisayar programcısı {} {} buldu.".format(self.programming, self.name, self.surname))


class Encapsulation(Python):
    def __init__(self, programming, name, surname, number,get, set):
        self.programming = programming
        self.name = name
        self.surname = surname
        self.number = number
        self.get = get
        self.set = set
        print("Öğretmen sınıfı çalıştı.")

    def info(self):
        print("{} {} {} Kapsülleme konusunda {} {} adında private değişkenleri public yapan {} metot oluşturmuştur..".format(self.programming, self.name, self.surname, self.get,self.set,self.number))


oh = Python("Guido", "van Rossum", 34)
no = Encapsulation("Python", "Guido","van Rossum",2, "get", "set")

oh.info()
no.info()