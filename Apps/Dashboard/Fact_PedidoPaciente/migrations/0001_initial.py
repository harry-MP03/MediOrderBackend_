# Generated by Django 4.2 on 2025-06-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='H_PEDIDOS_PACIENTE_DEST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeOrder', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': '[dbo].[H_PEDIDOS_PACIENTE_DEST]',
                'managed': False,
            },
        ),
    ]
