#Kristjan Moora
import math

class Kalkulaator:
    def __init__(self):
        pass
    
    def liitmine(self, x, y): #Liitmise funktsioon
        return x + y #Tagasta summa
    
    def lahutamine(self, x, y): #lahutamise funktsioon
        return x - y #Tagasta summa
    
    def korrutamine(self, x, y): #Korrutamise funktsioon
        return x * y #Tagasta summa
    
    def jagamine(self, x, y): #jagamise funktsioon
        if y != 0:
            return x / y  #Kui arv on suurem kui 0 tagasta summa
        else:
            return "Viga: Nulliga jagamine!" #Kui arv y = 0 tagastab programm veateate, et nulliga ei saa jagada
    
    def astendamine(self, x, y): #Astendamise funktsioon
        return x ** y #Tagasta aste
    
    def ruutjuur(self, x): #Ruutjuure funktsioon
        return math.sqrt(x) #Tagasta ruutjuur

#Loome kalkulaatori eksemplari
kalkulaator = Kalkulaator()

# Küsime kasutajalt soovitud funktsiooni ja numbrid
funktsioon = input("Vali funktsioon (liitmine, lahutamine, korrutamine, jagamine, astendamine, ruutjuur): ").strip().lower()
arv1 = float(input("Sisesta esimene number: "))
arv2 = float(input("Sisesta teine number: "))

# Valime kasutaja valitud funktsiooni ja kuvame vastuse
if funktsioon == "liitmine":
    tulemus = kalkulaator.liitmine(arv1, arv2)
elif funktsioon == "lahutamine":
    tulemus = kalkulaator.lahutamine(arv1, arv2)
elif funktsioon == "korrutamine":
    tulemus = kalkulaator.korrutamine(arv1, arv2)
elif funktsioon == "jagamine":
    tulemus = kalkulaator.jagamine(arv1, arv2)
elif funktsioon == "astendamine":
    tulemus = kalkulaator.astendamine(arv1, arv2)
elif funktsioon == "ruutjuur":
    tulemus = kalkulaator.ruutjuur(arv1)
else:
    tulemus = "Viga: Tundmatu funktsioon!" #Kui funktsiooni nimetus on valesti kirjutatud või funktsiooni lihtsalt ei ole siis tagastab programm veateate

# Kuvame tulemuse
print("Tulemus:", tulemus)

input() #Vajuta Enterit, et sulgeda programm