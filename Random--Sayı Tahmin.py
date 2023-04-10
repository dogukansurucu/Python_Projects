# bu kodumuzda öncelikle random modülünü import etmemiz gerekiyor.
# bunun için "import random" dememiz gerekir.
# daha sonra random modülündeki randint fonksiyonunu kullanarak belli sayı aralıklarında rastgele sayı üretiyoruz ve üretilen bu sayıyı tahmin etmemiz isteniyor.
# eğer sayıyı bilirsek programdan çıkılır. Sayıdan büyük bir sayı girmişsek daha küçük bir sayı giriniz , sayıdan küçük bir sayı girmişsek daha
# büyük bir sayı giriniz mesajı verilir.

import random

a = random.randint(1, 20)
b = 5
sayac = 0

while b > 0:
    sayi = int(input("Lütfen bir sayı giriniz: "))
    b -= 1
    sayac += 1

    if sayi == a:
        print(f"Tebrikler {sayac}.defada bildiniz! , kazandığınız puan: {100 - (100 / 5) * (sayac - 1)}")
        break
    elif sayi > a:
        print("Sayıyı azaltın")
    else:
        print("Sayıyı arttırın")

    if b == 0:
        print(f"Bilemediniz Üzgünüz , tahmin ettiğiniz sayı: {a}")