from django.db import models

# Create your models here.

class Categorie(models.Model):
     nom = models.CharField(max_length=30)
     img = models.ImageField(upload_to='img_cat/')

     active = models.BooleanField(default=True)

     def __str__(self):
         return self.nom
