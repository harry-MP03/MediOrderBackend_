# Generated by Django 4.2 on 2024-12-03 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PedidoPaciente', '0001_initial'),
        ('Historial_Medico', '0002_medical_history_active_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_history',
            name='orderFk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='PedidoPaciente.orderpatient', verbose_name='Pedido del Paciente'),
        ),
    ]