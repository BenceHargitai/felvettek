from django.shortcuts import render
from .models import Tanuló
# Create your views here.

def home_view(request, *args, **kwargs):
    mitortent = []
    if request.method =="POST":
        mitortent = Tanuló.bejelentkezes(request.POST)

    kontextus = {"Tanulók": Tanuló.objects.all(), "mitortent": mitortent}
    return render(request, "home.html", kontextus) 

def login_view(request, *args, **kwargs):
    return render(request, "belepve.html")