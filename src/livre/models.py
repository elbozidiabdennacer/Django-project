from django.db import models

from categorie.models import Categorie
# Create your models here.

class Livre(models.Model):
    titre = models.CharField(max_length=50)
    Auteur = models.CharField(max_length=50)
    date_edition = models.DateField()
    prix = models.FloatField()
    img = models.ImageField(upload_to='livre_img/')
    categorie = models.ForeignKey(Categorie , on_delete = models.PROTECT)

    def __str__(self):
        return self.titre
