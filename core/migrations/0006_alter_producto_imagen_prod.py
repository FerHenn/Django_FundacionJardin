# Generated by Django 4.0.4 on 2022-06-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_imagen_prod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_prod',
            field=models.ImageField(null=True, upload_to='Productos'),
        ),
    ]