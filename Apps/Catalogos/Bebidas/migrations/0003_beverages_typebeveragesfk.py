# Generated by Django 4.2 on 2024-10-26 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiposBebida', '0001_initial'),
        ('Bebidas', '0002_remove_beverages_typebeverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverages',
            name='typeBeveragesFK',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='TiposBebida.typebeverage', verbose_name='Tipo de bebida'),
        ),
    ]
