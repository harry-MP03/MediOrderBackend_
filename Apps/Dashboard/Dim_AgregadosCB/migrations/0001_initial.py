# Generated by Django 4.2 on 2025-06-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DIM_AGREGADOS_CB_DEST',
            fields=[
                ('idAggregates', models.IntegerField(primary_key=True, serialize=False)),
                ('codeAggregates', models.CharField(max_length=100)),
                ('foodName', models.CharField(max_length=60)),
                ('description_typefood', models.CharField(max_length=100)),
                ('Ingredients_food', models.CharField(max_length=120)),
                ('NameBeverage', models.CharField(max_length=60)),
                ('description_TypeBeverage', models.CharField(max_length=80)),
                ('Ingredients_Beverage', models.CharField(max_length=120)),
            ],
            options={
                'db_table': '[dbo].[DIM_AGREGADOS_CB_DEST]',
                'managed': False,
            },
        ),
    ]
