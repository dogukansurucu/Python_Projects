#Kullanıcıdan alınan bir sayının faktöriyeli gösteren kod


import math

try:
    sayi = int(input("sayi: "))
    k = 1

    assert sayi>=0,    "Negatif sayıların faktöriyeli alınmaz.."

    if sayi > 0:
        for i in range(k, sayi + 1):
            k *= i
        print(f"{sayi} sayısının faktöriyeli: {k} dir.")


    elif sayi == 0:
        print(math.factorial(0))

except (AssertionError,ValueError) as a:
    print("Hatanın Sebebi: ",a)
