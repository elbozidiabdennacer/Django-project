from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Panier
from .models import Commande
from client.models import Client
from livre.models import Livre
from .forms import PanieForm
from livre.views import listLivre
from .forms import CommandeForm
from django.utils import timezone

# Create your views here.

def setPanier(request, id):

    try:
        if request.session['idcl'] != None:
            idcl = request.session['idcl']
            cl = Client.objects.get(id=idcl)
            lvr = Livre.objects.get(id = id)

            cart, created = Panier.objects.get_or_create(pclient=cl)
            livres = [livre for livre in cart.plivre.all()]

            if not lvr in livres:
                livres.append(lvr)
                cart.plivre.set(livres)
                cart.save()

            '''if not lvr.id in cart:
                panie = Panier(pclient=cl, plivre=lvr)
                panie.save()'''

            '''if not lvr.id in cart:
                cart.add(lvr.id)'''

            return listLivre(request)

            '''cart = Panier.objects.filter(pclient=cl).values_list('plivre')
            if not lvr in cart:
                cart.append(lvr)
            #form = PanieForm(request.POST, pclient = cl, plivre = lvr)
            if form.is_valid():
                form.save()'''

    except KeyError:
        return render(request, 'signin.html')

def getPanier(request):
    try:
        if request.session['idcl'] != None:
            idcl = request.session['idcl']
            cl = Client.objects.get(id=idcl)
            panier, created = Panier.objects.get_or_create(pclient=cl)
            total = 0
            for livre in panier.plivre.all():
                total = total + livre.prix
            context = {
                'panier':panier.plivre.all() ,
                'total' : total
            }
            return render(request , 'panier.html' , context)

    except KeyError:
        return render(request, 'signin.html')



def rmLivre(request, id):

    try :
        idcl = request.session['idcl']
        cl = Client.objects.get(id=idcl)
        lvr = Livre.objects.get(id = id)

        panier = get_object_or_404(Panier , pclient=cl)
        panier.plivre.remove(lvr)
        return getPanier(request)
    except :
        return listLivre(request)


def setCommande(request):

    if request.session['idcl'] != None:
        idcl = request.session['idcl']
        cl = Client.objects.get(id=idcl)
        panier, created = Panier.objects.get_or_create(pclient=cl)
        cmd, created = Commande.objects.get_or_create(cmdclient=cl)
        for livre in panier.plivre.all():
            if not livre in cmd.cmdlivre.all():
                cmd.cmdlivre.add(livre)


        '''livres = [livre for livre in panier.plivre.all()]
        cmd, created = Commande.objects.get_or_create(cmdclient=cl)
        cmd.cmdlivre.set(livres)'''

        '''for ligne in panier:
            cmd.cmdlivre.add(ligne.plivre)'''
        cmd.save()
        panier.delete()

        return listLivre(request)
