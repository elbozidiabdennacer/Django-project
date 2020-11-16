from django.contrib import admin
from .models import Panier
from .models import Commande
# Register your models here.
class CmdeAdmin(admin.ModelAdmin):
    list_display = ['cmdclient','cmddate']
    search_fields = ['cmdclient']

admin.site.register(Panier)
admin.site.register(Commande,CmdeAdmin)
