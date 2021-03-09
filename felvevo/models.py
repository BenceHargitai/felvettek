from django.db import models
from django.shortcuts import render
from random import randrange

# Create your models here.
class Tanuló(models.Model):
    név = models.CharField(max_length=30)
    om = models.CharField(max_length=11)
    # nagyon gagyi így, listával jobb lenne na mindegy
    a = models.BooleanField()
    b = models.BooleanField()
    c = models.BooleanField()
    d = models.BooleanField()
    e = models.BooleanField()
    f = models.BooleanField()
    

    class Meta:
        verbose_name = ("Tanuló")
        verbose_name_plural = ("Tanulók")

    def __str__(self):
         return f"{self.név} | {self.om} | {self.a} | {self.b} | {self.c} | {self.d} | {self.e} | {self.f}"

    def feltoltes():
        with open('input.tsv', 'r') as f:
            for t in f.readlines():
                randomka = randrange(70000000000, 79999999999)
                tan = t.split('\t')
                nev = f"{tan[0]} {tan[1]}"
                if (tan[2]=="0"):
                    Tanuló.objects.create(név = nev, om =randomka, a = tan[3], b=tan[4], c=tan[5], d=tan[6], e=tan[7], f= tan[8])
                    print(f"{nev} nevű diákot hozzáadtam {randomka} OM azonosítóval!")
                else:
                    Tanuló.objects.create(név = nev, om =tan[2], a = tan[3], b=tan[4], c=tan[5], d=tan[6], e=tan[7], f= tan[8])
                    print(f"{nev} nevű diákot hozzáadtam {tan[2]} OM azonosítóval!")
            return 0

    def azonositas(name, azonosito):
        return Tanuló.objects.filter(név=name, om=azonosito).count()!=0

    def bejelentkezes(post):
        print("POST request érkezet!!! :)")
        teljes = f"{post['vnev']} {post['knev']}"
        azonosito = post['number']

        print(f"{teljes} felhasználónevű tanuló a {azonosito} OM-et beírva akar bejelentkezni")

        tlista = list(Tanuló.objects.filter(név=teljes, om=azonosito))
        if (teljes == "Add 1" and azonosito =="5"):
            print("--------Feltöltés elkezdve--------")
            Tanuló.feltoltes()
            print("--------Feltöltés befejezve--------")
            return 0

        if not Tanuló.azonositas(teljes, azonosito):
            print("sikertelen azonosítás!")
            return 0
        

        diak = tlista[0]
        print("sikeres azonosítás.")
        #print(diak)
        return True
        

    def adatoklekerese(azonosito):
        tlista = list(Tanuló.objects.filter(om=azonosito))
        return tlista[0]
		
