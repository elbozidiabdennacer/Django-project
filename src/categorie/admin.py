from django.contrib import admin

# Register your models here.
from .models import Categorie

class CatAdmin(admin.ModelAdmin):

    list_filter = ['active','nom']
    list_display = ['nom','active']
    search_fields = ['nom']

admin.site.register(Categorie , CatAdmin)
