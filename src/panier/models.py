from django.db import models
from django.utils import timezone


# Create your models here.
from client.models import Client
from livre.models import Livre

class Panier(models.Model):
    pclient = models.ForeignKey(Client , on_delete = models.CASCADE)
    plivre = models.ManyToManyField(Livre)

    def __str__(self):
        return self.pclient

class Commande(models.Model):
    cmdclient = models.ForeignKey(Client , on_delete = models.CASCADE)
    cmdlivre =models.ManyToManyField(Livre)
    cmddate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cmdclient
