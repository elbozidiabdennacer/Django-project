from django.conf.urls import url
from . import views

app_name = 'panier'

urlpatterns = [
        url(r'^getPanier$', views.getPanier, name='getPanier'),
        url(r'^(?P<id>\d+)$', views.setPanier, name='setPanier'),
        url(r'^delete/(?P<id>\d+)$', views.rmLivre, name='rmLivre'),
        url(r'^setCommande$', views.setCommande, name='setCommande'),
        ]
