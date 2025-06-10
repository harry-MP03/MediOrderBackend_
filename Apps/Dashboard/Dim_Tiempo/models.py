from django.db import models

class DIM_TIEMPO_DEST(models.Model):
    TiempoKey =models.IntegerField(primary_key=True)
    FechaCompleta = models.DateField()
    Anio = models.IntegerField()
    MesNumero =models.IntegerField()
    NombreMes = models.CharField(max_length=30)
    DiaDelMes = models.IntegerField()
    DiaSemanaNumero =models.IntegerField()
    NombreDiaSemana = models.CharField(max_length=30)
    TrimestreNumero = models.IntegerField()
    NombreTrimestre = models.CharField(max_length=62)
    SemanaDelAnioNumero = models.IntegerField()
    EsFinDeSemana = models.CharField(max_length=30)
    NombreEsFinDeSemana = models.CharField(max_length=2)

    class Meta:
        db_table = '[dbo].[DIM_TIEMPO_DEST]'
        managed = False

