#Kodun algoritması: Öncelikle şunu belirtmek istiyorum. Ben Pythonu Sadık Turan hocamdan öğrendim ve kursunu başarılı bir şekilde bitirdim.
# Öğrenme aşamasındayken Quiz algoritmasını ondan öğrenmiştim üzerine kendim birçok update bilgiler ekledim. Bu kodu hala geliştirme aşamasındayım.
# Fonksiyonel işlemleri json/text gibi veri saklama dosyalarıyla güncel tutmak istiyorum.Lafı çok uzatmadan dilerseniz yazdığım koda geçelim sevgili bağlantılarım..
# Quiz programı yapmak istiyoruz.Öncelikle  bunun için soruları,şıkları ve cevapları hazırlamamız lazım.
#Bu bilgiler A classında saklayıp B classında kullanmamız lazım. Öncelikle A classına verilerimizi gönderiyoruz ayrıca cevap doğru mu değil mi kontrol eden
#bir fonksiyon tanımlıyoruz.Daha sonra B classımızda soruları classlar yardımıyla aldıktan sonra soruları alma hazırlama kısmına geçiyoruz.
#Sorunun textini ve şıklarını yazdırmadan önce İndex numarasını belirlemek lazım bunu def init kısmında 0 olarak belirliyoruz.Her aldığımı soru sonrasında index numarası
#artacak bunun kodlarını da yazacağız.Şimdi soruyu dizayn etme aşamasındayız ondan sonra for döngüsüyle şıkları yazdırmalıyız.Daha sonra A classında tanımladığımız answer metodu aracılığıyla
#bir cevap yollayarak sorunun doğruluğunu kontrol ediyoruz.Doğruysa 20 puan kazanıyoruz ve bir sonraki soruya geçiyoruz.Ama şu soru
#akla gelmesi gerekir benim soru sayım yani question'nın len'i questionIndex ten küçük olursa quizdin bitmesi gerekir.question'ın len'i questionIndexden
#büyükse bir sonraki soru gelir.En son quiz bittiğinde yani question'nın len'i questionIndex'e eşit olursa totalde aldığımız puan gösterilir.


import random
import time

class Soru:
    def __init__(self,sorukismi,secenek,cevap):
        self.text = sorukismi
        self.choices = secenek
        self.answer = cevap

    def cevap_Kontrol(self,cevap):
        return self.answer == cevap


class Quiz:
    def __init__(self,sorular):
        self.questions = sorular
        self.score = 0
        self.questionIndex = 0

    def soru_Al(self):
        return self.questions[self.questionIndex]

    def soru_Goster(self):
        question = self.soru_Al()
        print(f'Soru {self.questionIndex+1} : {question.text}')

        k=1
        for i in question.choices:
            print(f"{k}-) {i}")
            k+=1

        answer = input("Cevabınız: ")

        if question.cevap_Kontrol(answer):
            self.score += 20

        self.questionIndex += 1

        self.soru_Yukle()


    def soru_Yukle(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.sorular_arasi_gecis()
            self.soru_Goster()

    def showScore(self):
        print('score: ',self.score)

    def sorular_arasi_gecis(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex

        if questionNumber > totalQuestion:
            time.sleep(2)
            print("Quiz bitti.")
        else:
            print(f"Soru:{questionNumber+1} hazıralanıyor....")
            time.sleep(1)
            print('\t\t\t3')
            time.sleep(1)
            print('\t\t\t2')
            time.sleep(1)
            print('\t\t\t1\n')
            print(f'\tQUESTİON {questionNumber+1} OF {totalQuestion} \t'.ljust(40,'|').rjust(60,'|'),'\n')


soru_secenekler_1 = [' "w" ',' "a" ',' "x" ',' "r" ',' "r+" ']
soru_secenekler_2 = [' dump() ',' load() ',' loads() ',' dumps() ']
soru_secenekler_3 = [' floor() ',' ceil() ',' gcd() ',' sqrt(x) ',' expm(x) ']
soru_secenekler_4 = [' String',' List',' Tuple ',' Unicode ',' Fronzenset ']
soru_secenekler_5 = [' Overloading',' Override',' Inheritance',' Encapsulation',' Polimorfizm ']

sorular_listesi = [soru_secenekler_1,soru_secenekler_2,soru_secenekler_3,soru_secenekler_4,soru_secenekler_5]

for i in sorular_listesi:
    random.shuffle(i)

q1 = Soru('Hangi print ile dosyaya girdi girmek erişme modu dosyaya veri eklerken önceki verileri silmeden ekler ? ',soru_secenekler_1,'"a"')
q2 = Soru('Aşağıdakilerden hangi Json fonksiyonu dictionary tipindeki veriyi json dosyasına kaydeder ? ',soru_secenekler_2,'dump()')
q3 = Soru('Pythonda Math modülünde hangi fonksiyon iki sayının ebobunu alır ? ',soru_secenekler_3,'gcd()')
q4 = Soru('Seçeneklerden hangisi Immutable nesnelerden biri değildir ? ',soru_secenekler_4,'List')
q5 = Soru('Aşağıdaki hangi konuda private durumdaki bilgileri almak için get() ve set() metodları kullanılır ? ',soru_secenekler_5,'Encapsulation')


sorular = [q1,q2,q3,q4,q5]

random.shuffle(sorular)

quiz = Quiz(sorular)

quiz.soru_Yukle()