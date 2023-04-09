# 2 sayı arasındaki sayıların asal olup olmadığını gösteren uygulamalar yaptım.



"""
2 den başka çift olup asal olan başka bir sayı olmadığı için bu yöntem daha kullanışlı.

en iç blokta asallığı kontrol edilen sayının kendinden önceki 1 den büyük ve pozitif sayılar dönerken bu sayılara bölümünden kalan
0 ise yani çarpanlarından biri var ise asal değildir deyip break ile içteki for döngüsünü durdurup üstteki for döngüsüyle bir sonraki değer döndürülmeli.
Ama sayı çarpanlarından biriyle karşılaşmamış ise if bloğunda sayı boş döner ve döngünün bitmesiyle içteki for döngüsünden çıkılır,
else bloğuna girilir ve asal sayıdır ifadesi yazdırılır.

2 sayısı ise zaten en içteki for'a giremediğinden else bloğuna girer ve asaldır ifadesini döndürür.
"""

number1 = int(input("1.sayı: "))
number2 = int(input("2.sayı: "))

def a(x,y):
    for a in range(int(x + 1), int(y)):
        if a > 1:
            for b in range(2, a):
                if a%b == 0:
                    print(f"{a} asal değildir.")
                    break
            else:
                print(f"{a} asaldır.")
        else:
            print(f"{a} asal değildir.")

a(number1,number2)
print("\n")






"""
tek olan asal sayılar en içteki for'un if bloğunda continue ile başa dönüyor ve for döngüsünün bitmesiyle else bloğuyla
asal sayıdır ifadesi gösteriliyor.

tek sayı olup asal olmayan sayılarda (mesela 9) ise '2 3 4 ... 9' çarpanlarından birine denk gelirse ('3' ün katı) en iç for'daki else bloğuna girer
ve asal değildir ifadesi döner ve döngüden çıkar.

2 sayısı ise zaten en içteki for'a giremediğinden else bloğuna girer ve asaldır ifadesini döndürür.
"""

number1 = int(input("1.sayı: "))
number2 = int(input("2.sayı: "))

def b(x,y):
    for b in range(int(x + 1), int(y)):
        if b > 1:
            for c in range(2, b):
                if b%c != 0:
                    continue
                else:
                    print(f"{b} asal değildir.")
                    break
            else:
                print(f"{b} asaldır.")
                continue
        else:
            print(f"{b} asal değildir.")

b(number1,number2)
