from django.db import models

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
         return f"{self.név} - {self.om}"

    def azonositas(name, azonosito):
        return Tanuló.objects.filter(név=name, om=azonosito).count()!=0

    def bejelentkezes(post):
        print("POST request érkezet!!! :)")
        teljes = f"{post['vnev']} {post['azonosito']}"

        print(f"{teljes} felhasználónevű tanuló a OM-et beírva akar bejelentkezni")

        #tlista = list(Tanulo.objects.filter(név=post['teljes'], om=post['azonosito']))

        #if not Tanulo.azonositas(post['teljes'], post['azonosito']):
         #   print("sikertelen azonosítás!")
          #  uzenetek.append("Hibás a felhasználónév vagy a jelszó!")
           # return 0

        #diak = tlista[0]
       # print("sikeres azonosítás.")
		
