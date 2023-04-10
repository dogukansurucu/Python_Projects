# bu kodumuzda private olarak tanımlanmış bir özelliği nasıl public hale getirerek
# ulaşılabilir hale getirebilirizi anlatmaya çalıştım. private durumdaki self.__age = adında yaş bilgisine
# erişebilmek için get ve set metodlarını kullanırız.
# Ayrıca Private,Protected ve public gibi üyelerle ilgili birçok detaya değinmiş olduk.

class Student:
    def __init__(self, name, age):

        self.name = name   # public member
        self.__age = age   # private member
        self._number = 25  # protected member

    def c(self):
        print(self._number) # protected üye
        print(self.__age)  # private haldeki üyeyi sadece sınıf içerisinde kullanabiliriz. Sınıf dışında kullanmak için get ve set metodunu kullanırız.

    # get() method
    def get_age(self):
        return self.__age

    def getNumber(self):
        return self._number

    # set() method
    def set_age(self, age):
        self.__age = age


stud = Student('Jessa', 14)

stud.c()

print('Name:', stud.name, stud.get_age())


print(stud._number)
print(stud.getNumber())


# set() kullanarak privat haldeki değişkeninin değerini değiştiririz.
stud.set_age(16)

# get() metodunu kullanarak private haldeki değişkene erişebiliriz.
print('Name:', stud.name, stud.get_age())


