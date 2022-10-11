# üniversitede sınav sistemini baz aldım. Üniversitede her dersin vize,final,quiz ve lab notlarının ortalaması alınarak dönem sonu o dersin notu belli olmuş
# olur. Her üniversitede sınavların yüzdelik dilimleri farklı olurken kendi üniversitemi baz alarak kodladığım bu programda vizelerin ortalamasının
# %30 u , finalin %50 si , quizlerin %5 ve labların %15 u alınır.Bu yüzdelik dağılım genellikle böyle olmakla beraber 
# hocadan hocaya nadir de olsa değişiklik göstermektedir.

vize_1 = int(input("1.vize notunuz : "))
vize_2 = int(input("2.vize notunuz : "))
quiz1 = int(input("quiz-1 notunuz : "))
final = int(input("final notunuz : "))
quiz2 =int(input("quiz-2 notunuz : "))
lab1 = int(input("Lab-1 notunuz : "))
lab2 = int(input("Lab-2 notunuz : "))

ort_Hesapla = float(((vize_1+vize_2)/2)*(0.30) + final*(0.50) + ((quiz1+quiz2)/2)*0.05 + ((lab1+lab2)/2)*0.15)


if 0<=ort_Hesapla and ort_Hesapla<39.50:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz FF")
elif 39.50<=ort_Hesapla and ort_Hesapla<45:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz FD")
elif 45.00 <= ort_Hesapla and ort_Hesapla <50:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz DD")
elif 50.00 <= ort_Hesapla and ort_Hesapla < 60:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz DC")
elif 60.00 <= ort_Hesapla and ort_Hesapla < 65:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz CC")
elif 65.00 <= ort_Hesapla and ort_Hesapla < 75:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz CB")
elif 75.00 <= ort_Hesapla and ort_Hesapla < 85:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz BB")
elif 85.00 <= ort_Hesapla and ort_Hesapla < 90:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz BA")
elif 90 <= ort_Hesapla and ort_Hesapla < 100:
    print(f"ortalamanız {ort_Hesapla} ve Harf notunuz AA")

else:
    print('beklenmeyen sonuç')
