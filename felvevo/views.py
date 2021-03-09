from django.shortcuts import render
from .models import Tanuló
# Create your views here.

def home_view(request, *args, **kwargs):
    mitortent = []
    if request.method =="POST":
        if (Tanuló.bejelentkezes(request.POST) == True):
            adatok = Tanuló.adatoklekerese(request.POST['number'])
            x = str(adatok). replace('<','').replace('>','').split('|') 
            kontextus = {
                "név" : x[0],
                "om" : x[1],
                "a" : x[2].replace(" ",""),
                "b" : x[3].replace(" ",""),
                "c" : x[4].replace(" ",""),
                "d" : x[5].replace(" ",""),
                "e" : x[6].replace(" ",""),
                "f" : x[7].replace(" ",""),
            }
            print(kontextus)
            return render(request, "belepve.html", kontextus)

    kontextus = {
        
    }
    return render(request, "home.html", kontextus) 

