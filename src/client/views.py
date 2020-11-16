from django.shortcuts import render
from django.contrib import messages

from .forms import ClientForm
from .models import Client
from livre.views import listLivre

def Signup(request):

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

    else :
        form = ClientForm()

    context = {
        'form':form
    }

    return render(request , 'signup.html', context)

def Signin(request):
    em = request.POST.get('email')
    if em != None:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            cl = Client.objects.get(email=email, password=password)
            request.session["idcl"] = cl.id
            request.session["fullname"] = cl.nom +" "+cl.prenom
            return listLivre(request)
        except Client.DoesNotExist:
            #messages.add_message(request, messages.ERROR, 'Hello world.')
            messages.error(request, 'Mot de passe ou email incorrect.')
            return render(request , 'signin.html')
    return render(request , 'signin.html')

def Logout(request):
    #for sesskey in request.session.keys():
        #del request.session[sesskey]
    request.session.clear()
    return listLivre(request)
