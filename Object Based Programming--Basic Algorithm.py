# Pythonda nesne tabanlı programlamaya güzel basic bir örnek
# Add adında bir class oluşturup bu classa kullanıcıdan 2 sayı alıp fonksiyonlar ve metodlar yardımıyla toplamı alınır.
# Tabi öncelikle classımızı inceleyelim. öncelikle yapıcı metotdan önce class attribute ve class olmayan attributes bölümü vardır.Class seviyesinde
# olmayan attributes'da firs second answer değişkenlerini tanımladık , bunları niçin yaptık peki ?
# dediğimiz gibi kullanıcıdan aldığımız sayıları farklı fonksiyonda topladık ve bu fonksiyonu çağırmazsak iki sayı toplanmaz ve diğer fonksiyon
# çağırdığında çalışır.çalıştığında ise calculate() fonksiyonunu çağırmadığımızdan dolayı iki sayı devreye girmez.Classın attribute kısmında
# tanımladığımız first,second ve answer değişkenleri çağrılır.

class Add:
    # öznitelikleri başlatma yordamı
    # class object attributes(class seviyesinde)
    first = 0
    second = 0
    answer = 0

    # object attributes(class seviyesinde değil)
    # constructor ( yapıcı metod )
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def display(self):
        print("ilk sayı = " + str(self.first))
        print("ikinci sayı = " + str(self.second))
        print("iki sayının toplamı = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second



sayi1 = int(input("1.sayıyı giriniz: "))
sayi2 = int(input("2.sayıyı giriniz: "))

#Sınıfın bir nesnesini oluşturur
obj = Add(sayi1,sayi2)

obj.calculate()
obj.display()