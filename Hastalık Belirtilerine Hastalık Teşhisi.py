# Hastalık belirtilerine göre hastalık teşhisi algoritmasıyla yazdığım bir kod.
# NEZLE : Ateş,Boğaz ağrısı,burun akıntısı,hapşırma,kuru öksürük,gözlerde sulanma,baş ağrısı gibi beliritielri vardır.
# ALERJİ : Kaşıntı,öksürük,hapşırma ve nefes darlığı gibi belirtileri vardır.
# GRİP : Ateş,baş ağrısı,öksürük vb belirtileri vardır.
# COVİD-19 : Ateş,nefes darlığı,öksürük,tat alma kaybı gibi belirtileri vardır.


burun_akintisi = int(input("burun akıntısı belirtisi varsa 1 yoksa 0 yazınız: "))
hapsirik = int(input("hapşırık belirtisi varsa 1 yoksa 0 yazınız: "))
goz_kizarikligi = int(input("göz kızarıklı belirtisi varsa 1 yoksa 0 yazınız: "))
kasinti = int(input("kaşıntı belirtisi varsa 1 yoksa 0 yazınız: "))
bas_Bogaz_Agrisi = int(input("baş boğaz ağrısı belirtisi varsa 1 yoksa 0 yazınız: "))
nefes_darligi = int(input("nefes darlığı belirtisi varsa 1 yoksa 0 yazınız: "))
ani_ates = int(input("hırıltı belirtisi varsa 1 yoksa 0 yazınız: "))
halsizlik = int(input("halsizlik belirtisi varsa 1 yoksa 0 yazınız: "))
kuru_oksuruk = int(input("kuru öksürük belirtisi varsa 1 yoksa 0 yazınız: "))

if burun_akintisi==1 and hapsirik==1 and goz_kizarikligi==1 and kasinti==1 and bas_Bogaz_Agrisi==1 and nefes_darligi==0 and ani_ates==0 and halsizlik==0 and kuru_oksuruk==0 :
    print("Yüksek ihtimal Nezlesiniz")
elif burun_akintisi==0 and hapsirik==1 and goz_kizarikligi==1 and kasinti==1 and bas_Bogaz_Agrisi==0 and nefes_darligi==0 and ani_ates==0 and halsizlik==0 and kuru_oksuruk==1 :
    print("Yüksek ihtimal Alerjiniz var")
elif burun_akintisi == 0 and hapsirik == 0 and goz_kizarikligi == 0 and kasinti == 0 and bas_Bogaz_Agrisi == 1 and nefes_darligi == 0 and ani_ates == 1 and halsizlik == 1 and kuru_oksuruk == 1:
    print("Yüksek ihtimal Gripsiniz")
elif burun_akintisi==0 and hapsirik==0 and goz_kizarikligi==0 and kasinti==0 and bas_Bogaz_Agrisi==0 and nefes_darligi==1 and ani_ates==1 and halsizlik==1 and kuru_oksuruk==1 :
    print("Yüksek ihtimal Covid-19 geçiriyorsunuz")
else:
    print("değişken semptomlar algılandı bilmediğimiz bir hastalık olabilir.")
