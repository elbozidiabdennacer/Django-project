from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
        url(r'^signup$', views.Signup, name='signup'),
        url(r'^signin$', views.Signin, name='signin'),
        url(r'^logout$', views.Logout, name='logout')      
]
