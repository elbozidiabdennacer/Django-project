# Generated by Django 3.1.2 on 2020-10-26 20:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='cmddate',
            field=models.DateField(verbose_name=datetime.datetime(2020, 10, 26, 20, 45, 39, 917101, tzinfo=utc)),
        ),
    ]
