# Bu basic projemizde Recursive functions konusunu ele aldık.
# bu kodu yazmamızdaki amacımız iki sayı arasında ardışık bir düzen oluşturma.
# kullanıcıdan 3 parametre alıcaz. 1.sayı büyük değer, 2.sayı küçük değer ve 3.sayı 1.sayıdan 2.sayıya kadar
# kaçar kaçar azalacağını gösteren bir sayı olacak.Eğer 1.parametre 2.parametreden küçük olursa boş liste döndürecek
# koşullar uygun bir şekilde gerçekleşirse fonksiyon return ifadesiyle tekrar çağrılacak tabi bu esnada boş liste dönene kadar
# her azalmada elemanlar listeye atılacak.

buyuk_Sayi = int(input("Büyük sayıyı giriniz: "))
kucuk_Sayi = int(input("Küçük sayıyı giriniz: "))
azalan_Miktar = int(input("Sayı ne kadar azalarak gerilesin: "))

def arasi(x, y, azalanMiktar):
    if x < y:
        return []
    else:
        return [x] + arasi(x-azalanMiktar,y, azalanMiktar)

print(arasi(buyuk_Sayi,kucuk_Sayi,azalan_Miktar))