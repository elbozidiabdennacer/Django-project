# Generated by Django 3.1.2 on 2020-10-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]