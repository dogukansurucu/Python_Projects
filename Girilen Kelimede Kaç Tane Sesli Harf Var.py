# kullanıcının girdiği bir kelimedeki sesli harfleri sayan bir kod parçacığı
# Sesli harfler a,e,ı,i,o,ö,u,ü harfleridir ve biz kullanıcıdan bir kelime istediğimizde bu kelimede kaç tane sesli harf
# olduğunu bulan bir program yazdım.Yalnız bizim yazdığımız kelimeler büyük harf küçük harf ile yazılmış da olabilir. Bunun için büyük harfleri de string
# içine dahil ettik ve kelimedeki hangi harfler sesli ise yanına kaçıncı sesli harf olduğunu yazdırmış olacağız.Sonuç olarak kaç tane sesli harf olduğunu görmüş olacağız.


kelime = input("kelimeyi giriniz: ")
sesli_harfler = 'aeıioöuüAEIİOÖUÜ'

liste = []
for i in kelime:
    if i in sesli_harfler:
        liste.append(i)
print("kelime:",kelime," ",liste," ","Sesli Harf Sayıs:",len(liste))
