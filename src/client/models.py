from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email =  models.EmailField(max_length=100)
    tel = PhoneNumberField(null=False, blank=False, unique=True, region="MA")
    password =models.CharField(max_length=50)

    def __str__(self):
        return self.nom
