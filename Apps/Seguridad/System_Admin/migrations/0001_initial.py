# Generated by Django 4.2 on 2024-10-02 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='systemAdmin',
            fields=[
                ('idAdmin', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('namesAdmin', models.CharField(max_length=60, verbose_name='Nombres del encargado')),
                ('lastNameAdmin', models.CharField(max_length=60, verbose_name='Apellidos del encargado')),
                ('phoneAdmin', models.CharField(max_length=15, verbose_name='Teléfono del encargado')),
                ('Username', models.CharField(max_length=15, verbose_name='Nombre de Usuario')),
                ('password', models.CharField(max_length=15, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name_plural': 'Encargados',
            },
        ),
    ]
