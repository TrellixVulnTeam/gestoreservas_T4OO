# Generated by Django 2.1.7 on 2019-03-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0017_auto_20190327_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='estacionamiento',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='fumar',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='tarjetas',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='wifi',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=20),
        ),
    ]