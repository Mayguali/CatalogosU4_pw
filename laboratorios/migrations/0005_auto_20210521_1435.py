# Generated by Django 3.2 on 2021-05-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0004_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Fecha_salida',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='num_control',
            field=models.CharField(max_length=10),
        ),
    ]
