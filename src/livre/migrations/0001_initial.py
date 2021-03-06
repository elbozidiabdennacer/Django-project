# Generated by Django 3.1.2 on 2020-10-21 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('Auteur', models.CharField(max_length=50)),
                ('date_edition', models.DateField()),
                ('prix', models.FloatField()),
                ('img', models.ImageField(upload_to='livre_img/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categorie.categorie')),
            ],
        ),
    ]
