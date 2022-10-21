# 2 sayı arasındaki sayıların asal olup olmadığını gösteren algoritma
sayi1 = int(input('number 1:'))
sayi2 = int(input('number 2:'))


def asal(number1, number2):
    for number in range(number1, number2 + 1):
        if number > 1:
            ''' üstteki satırdaki koddaki olay şu: iki sayı arasındaki asalları bulacağımızdan ve de asallar pozif olduğundan dolayı sayılar 1 den büyük olmak zorunda'''
            for i in range(2, number):
                if number % i == 0:
                    print(f"{number} asal değildir.")
                    break
            else:
                print(f"{number} asal sayıdır.")
        else:
            print(f"{number} asal değildir.")

asal(sayi1, sayi2)
