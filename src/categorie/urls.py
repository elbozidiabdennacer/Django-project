from django.conf.urls import url
from . import views

app_name = 'categorie'

urlpatterns = [
        url(r'^$', views.allCat, name='categories'),
]
