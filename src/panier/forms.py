from django import forms
from .models import Panier
from .models import Commande


class PanieForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = '__all__'

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
