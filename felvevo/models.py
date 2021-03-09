from django.db import models

# Create your models here.
class Tanuló(models.Model):
    név = models.CharField(max_length=30)
    om = models.IntegerField()
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

    

