from django.shortcuts import render
from .models import Tanuló
# Create your views here.

def home_view(request, *args, **kwargs):
    mitortent = []
    if request.method =="POST":
        if (Tanuló.bejelentkezes(request.POST) == True):
            adatok = Tanuló.adatoklekerese(request.POST['number'])
            info = str(adatok[0]).replace('<','').replace('>','').split('|') 
            count = 0
            
            array = []
            for k in adatok:
                szakok = {}
                info = str(adatok[count]).replace('<','').replace('>','').split('|') 
                szak = info[2].replace(" ","")
                felveve = info[3].replace(" ","")
                szakok["szak"] = szak
                szakok["dontes"] = felveve
                array.append(szakok)
                count = count + 1
            kontextus = {
                "név" : info[0],
                "om" : info[1].replace(" ",""),
                "szakok" : array
            }
            print (kontextus)
            return render(request, "belepve.html", kontextus)

    kontextus = {
        
    }
    return render(request, "home.html", kontextus) 

