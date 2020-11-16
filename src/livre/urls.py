from django.conf.urls import url
from . import views

app_name = 'livre'

urlpatterns = [
        url(r'^$', views.listLivre, name='listLivre'),
        url(r'^details/(?P<id>\d+)$', views.detLivre, name='detLivre'),
        url(r'^categorie/(?P<id>\d+)$', views.LivreCat, name='LivreCat'),
        url(r'^search/$', views.Search, name='search'),
]
