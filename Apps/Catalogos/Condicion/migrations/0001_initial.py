# Generated by Django 4.2 on 2024-10-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='condition_lvl',
            fields=[
                ('idcondition_lvl', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ConditionName', models.CharField(max_length=20, verbose_name='Nombre de condition')),
            ],
            options={
                'verbose_name': 'Condiciones',
            },
        ),
    ]
