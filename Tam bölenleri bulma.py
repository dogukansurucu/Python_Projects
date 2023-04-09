## kullanıcıdan aldığımız bir sayının tam bölenlerini bulma

a = int(input("sayıyı giriniz: "))
liste = []

def b(sayi=a):
    for i in range(-sayi,sayi+1):
        if i==0:
            continue
        if sayi%i==0:
            liste.append(i)

b(a)
print(liste)




## kullanıcıdan aldığımız bir sayının pozitif bölenlerini bulma

sayi = int(input('sayi: '))
def TamBolenleribul(sayi):
    tamBolenler = []

    for i in range(1,sayi+1):
        if (sayi%i==0):
            tamBolenler.append(i)
        else:
            continue

    return tamBolenler

result = TamBolenleribul(sayi)
print(result)
