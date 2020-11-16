from django.shortcuts import render

# Create your views here.
from .models import Categorie

def allCat(request):
    #allCat = Categorie.objects.all()
    allCat = Categorie.objects.filter(active=True)

    context = {
        'allCat':allCat ,
    }

    return render(request , 'Categories.html' , context)
