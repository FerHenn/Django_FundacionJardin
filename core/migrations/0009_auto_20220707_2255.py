# Generated by Django 3.2.13 on 2022-07-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220707_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='id Cliente')),
                ('rut_cli', models.CharField(max_length=11, verbose_name='Rut Cliente')),
                ('nombre_cli', models.CharField(max_length=40, verbose_name='Nombre_prod')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('direccion', models.CharField(max_length=40, verbose_name='Direccion Cli')),
                ('password_cli', models.CharField(default='12345', max_length=40, null=True, verbose_name='Contraseña')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
