# Generated by Django 4.0.4 on 2022-06-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220605_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion_prod',
            field=models.TextField(verbose_name='Descripcion'),
        ),
    ]