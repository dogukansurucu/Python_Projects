# githubdan requests modülü ile veri alış-verişinde bulunmak için öncelikle github doc sayfasına gidip api bilgilerini öğrenmemiz gerekir.
# requests.get(),requests.put(),requests.post() gibi metodlarla hangi verileri çekebileceğimizi hangi verileri güncelleyip gönderebileceğimiz döküman sayfasında
# yazıyor.Bu kodda temel parçacık api url ve gerektiğinde hesabımın bana ait olduğunu doğrulatmak amacıyla oluşturduğum tokeni
# fonksiyonlarda kullanmak için classın içinde tanımladım.Sonrası rutin requests metodlarını uygulamak oluyor.

# !!! veri alış-verişi için eski github hesabımı kullanmıştım.

import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        #oluşturduğun token ile senin hesabın olduğu anlaşılabiliyor.
    def getUser(self,username):
        response = requests.get(self.api_url+'/users/' +username)
        return response.json()
        #json.loads şeklinde de yapabilirdin.
    def getRepositories(self,username):
        response_1 = requests.get(self.api_url+'/users/'+username+'/repos')
        return response_1.json()
    def createRepository(self,name):
        response_2 =requests.post(self.api_url+'/user/repos?access_token'+self.token,json = {
            "name" : name,
            "description":  "create Repository",
            "homepage" : "https://github.com/dogukansurucu",
            "auto_init": True,
            "private" : False,
            "has_issues" : True,
            "has_project" : True,
            "has_wiki" : False
        })
        return response_2.json()



result = Github()

while True:
        print("MENÜ".center(50, '*'))
        secim = input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçiminiz: ")

        if secim == '4':
            break
        else:
            if secim == '1':
                username = input('İsim giriniz: ')
                result_1 = result.getUser(username)
                print(f"name: {result_1['name']} id: {result_1['id']} following: {result_1['following']} follower: {result_1['followers']} \n"
                      f"for more information, {result_1['html_url']}")
            elif secim == '2':
                username = input('İsim giriniz: ')
                result_2 = result.getRepositories(username)
                for repo in result_2:
                    print(repo['name'],':',repo['private'])

            elif secim == '3':
                name = input("repository name : ")
                result_3 = result.createRepository(name)
                print(result_3)
            else:
                print("Böyle bir seçim yok.")
