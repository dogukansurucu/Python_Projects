# Kullanıcıdan bir parola alınız ve bu parolada türkçe karakter içeriyorsa hata mesajı oluşturunuz. aldığımız parola i for ile
# i değişkenine atarken her bir karakter tr_karakterin içinde var mı bakılıyor yoksa else ile döngü boş geçiliyor ve i bir sonraki karaktere
# geçiyor yine aynı şekilde tr_karakterin içinde var mı diye bakıyoruz.. Bu süreç karakterin leni bitene kadar devam ediyor. En son döngü
# bittiğinde parolamızda hiç türkçe karakter yoksa parola kabul edildi çıktısını veriyoruz.


tr_karakter = "şŞçÇğĞüÜöÖıi"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise Exception("Parolada Türkçe karakter kullanılamaz!")
    else:
        continue

print("Parola kabul edildi!")