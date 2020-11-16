from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_list_or_404
from .models import Livre
from categorie.models import Categorie
import re

# Create your views here.


def listLivre(request):

    listLivre = Livre.objects.all()
    context = {
        'listLivre':listLivre ,
    }

    return render(request , 'index.html' , context)

def detLivre(request , id):

    try:
        if request.session['idcl'] != None:
            detLivre = Livre.objects.get(id=id)
            context = {
                'detLivre':detLivre ,
            }
            return render(request , 'details.html' , context)

    except KeyError:
        return render(request, 'signin.html')

def LivreCat(request , id):

    cat = Categorie.objects.get(id=id)
    listLivre = Livre.objects.filter(categorie = cat)
    #cat = Categorie.objects.get(id=idcat)
    context = {
      'listLivre':listLivre,
      'cat':cat,
    }
    return render(request, 'Categorie.html', context)

def Search(request):
    mot = request.POST.get('search')

    if mot:
        results = []
        article_list = get_list_or_404(Livre)
        for article in article_list:
            if re.findall(mot, article.titre):
                results.append(article)
        '''for article in results:
            article.body = markdown.markdown(article.body, )
        tag_list = Tag.objects.all().order_by('name')'''

        return render(request, 'search.html', {'article_list': results})
    else:
        return listLivre(request)
