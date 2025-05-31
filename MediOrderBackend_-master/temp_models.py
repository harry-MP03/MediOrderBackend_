# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgregadoscBAggregatesCb(models.Model):
    idaggregates = models.AutoField(db_column='idAggregates', primary_key=True)  # Field name made lowercase.
    codeaggregates = models.CharField(db_column='codeAggregates', unique=True, max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    beveragefk = models.ForeignKey('BebidasBeverages', models.DO_NOTHING, db_column='beverageFK_id')  # Field name made lowercase.
    foodfk = models.ForeignKey('ComidasFoods', models.DO_NOTHING, db_column='foodFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgregadosC_B_aggregates_cb'


class BebidasBeverages(models.Model):
    idbeverages = models.AutoField(db_column='idBeverages', primary_key=True)  # Field name made lowercase.
    namebeverage = models.CharField(db_column='NameBeverage', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    beverage_description = models.CharField(db_column='Beverage_description', max_length=110, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    ingredients_beverage = models.CharField(db_column='Ingredients_Beverage', max_length=120, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    typebeveragesfk = models.ForeignKey('TiposbebidaTypebeverage', models.DO_NOTHING, db_column='typeBeveragesFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bebidas_beverages'


class CamasBeds(models.Model):
    idbed = models.AutoField(primary_key=True)
    bedcode = models.CharField(db_column='bedCode', unique=True, max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    careunitfk = models.ForeignKey('UnidadescuidadosCareunit', models.DO_NOTHING, db_column='CareUnitFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Camas_beds'


class ComidasFoods(models.Model):
    idfood = models.AutoField(db_column='idFood', primary_key=True)  # Field name made lowercase.
    foodname = models.CharField(db_column='foodName', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fooddescription = models.CharField(db_column='foodDescription', max_length=110, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    ingredients_food = models.CharField(db_column='Ingredients_food', max_length=120, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    typefoodfk = models.ForeignKey('TiposcomidaTypefood', models.DO_NOTHING, db_column='typeFoodFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comidas_foods'


class CondicionConditionLvl(models.Model):
    idcondition_lvl = models.AutoField(primary_key=True)
    conditionname = models.CharField(db_column='ConditionName', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Condicion_condition_lvl'


class DetallesenfermedadDetaildisease(models.Model):
    iddetaildisease = models.AutoField(db_column='idDetailDisease', primary_key=True)  # Field name made lowercase.
    diseasefk = models.ForeignKey('EnfermedadesDiseases', models.DO_NOTHING, db_column='diseaseFK_id')  # Field name made lowercase.
    patient_dfk = models.ForeignKey('PacientePatient', models.DO_NOTHING, db_column='patient_dFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetallesEnfermedad_detaildisease'


class EnfermedadesDiseases(models.Model):
    iddisease = models.AutoField(db_column='idDisease', primary_key=True)  # Field name made lowercase.
    namedisease = models.CharField(db_column='nameDisease', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    typediseasefk = models.ForeignKey('TiposenfermedadesTypedisease', models.DO_NOTHING, db_column='typeDiseaseFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enfermedades_diseases'


class ExpedientepacienteExpedientpatient(models.Model):
    idexpedient = models.AutoField(db_column='idExpedient', primary_key=True)  # Field name made lowercase.
    codeexpedient = models.CharField(db_column='codeExpedient', unique=True, max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    reasonconsult = models.CharField(db_column='reasonConsult', max_length=80, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    diagnosis = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS')
    treatment = models.CharField(max_length=60, db_collation='Modern_Spanish_CI_AS')
    dietaryrestrictions = models.CharField(db_column='dietaryRestrictions', max_length=200, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    dietarypreferences = models.CharField(db_column='dietaryPreferences', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    attedingphysician = models.CharField(db_column='attedingPhysician', max_length=85, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    conditionfk = models.ForeignKey(CondicionConditionLvl, models.DO_NOTHING, db_column='conditionFK_id')  # Field name made lowercase.
    detaildiseasefk = models.ForeignKey(DetallesenfermedadDetaildisease, models.DO_NOTHING, db_column='detailDiseaseFK_id')  # Field name made lowercase.
    patientfk = models.ForeignKey('PacientePatient', models.DO_NOTHING, db_column='patientFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpedientePaciente_expedientpatient'


class HistorialMedicoMedicalHistory(models.Model):
    idmedicalhistory = models.AutoField(db_column='idMedicalHistory', primary_key=True)  # Field name made lowercase.
    codehistory = models.CharField(db_column='codeHistory', unique=True, max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    datehistory = models.DateField(db_column='dateHistory')  # Field name made lowercase.
    bedfk = models.ForeignKey(CamasBeds, models.DO_NOTHING, db_column='bedFK_id')  # Field name made lowercase.
    expedientp_fk = models.ForeignKey(ExpedientepacienteExpedientpatient, models.DO_NOTHING, db_column='expedientP_FK_id')  # Field name made lowercase.
    orderfk = models.ForeignKey('PedidopacienteOrderpatient', models.DO_NOTHING, db_column='orderFk_id')  # Field name made lowercase.
    active_patient = models.BooleanField(db_column='active_Patient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historial_Medico_medical_history'


class PacientePatient(models.Model):
    idpatient = models.AutoField(primary_key=True)
    namespatient = models.CharField(db_column='namesPatient', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    lastnamepatient = models.CharField(db_column='lastnamePatient', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    cedulapatient = models.CharField(db_column='cedulaPatient', max_length=14, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    genderpatient = models.CharField(db_column='genderPatient', max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    agepatient = models.IntegerField(db_column='agePatient')  # Field name made lowercase.
    phonepatient = models.CharField(db_column='phonePatient', max_length=15, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Paciente_patient'


class PedidopacienteOrderpatient(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    codeorder = models.CharField(db_column='codeOrder', unique=True, max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    orderstatus = models.CharField(db_column='orderStatus', max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    quantity = models.IntegerField()
    dateorder = models.DateField(db_column='dateOrder')  # Field name made lowercase.
    adminfk = models.ForeignKey('SystemAdminSystemadmin', models.DO_NOTHING, db_column='adminFK_id')  # Field name made lowercase.
    aggregatesfk = models.ForeignKey(AgregadoscBAggregatesCb, models.DO_NOTHING, db_column='aggregatesFK_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoPaciente_orderpatient'


class SystemAdminSystemadmin(models.Model):
    idadmin = models.AutoField(db_column='idAdmin', primary_key=True)  # Field name made lowercase.
    namesadmin = models.CharField(db_column='namesAdmin', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    lastnameadmin = models.CharField(db_column='lastNameAdmin', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    phoneadmin = models.CharField(db_column='phoneAdmin', max_length=15, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=80, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    password_admin = models.CharField(db_column='Password_admin', max_length=15, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'System_Admin_systemadmin'


class TiposbebidaTypebeverage(models.Model):
    id_typebeverage = models.AutoField(db_column='id_typeBeverage', primary_key=True)  # Field name made lowercase.
    description_typebeverage = models.CharField(db_column='description_TypeBeverage', max_length=80, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposBebida_typebeverage'


class TiposcomidaTypefood(models.Model):
    idtypefood = models.AutoField(db_column='idTypeFood', primary_key=True)  # Field name made lowercase.
    description_typefood = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'TiposComida_typefood'


class TiposenfermedadesTypedisease(models.Model):
    idtype = models.AutoField(primary_key=True)
    nametype = models.CharField(max_length=60, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'TiposEnfermedades_typedisease'


class UnidadescuidadosCareunit(models.Model):
    idcareunit = models.AutoField(db_column='idCareunit', primary_key=True)  # Field name made lowercase.
    namecareunit = models.CharField(db_column='nameCareUnit', max_length=250, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadesCuidados_careunit'


class UsuariosUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Usuarios_user'


class UsuariosUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsuariosUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Usuarios_user_groups'
        unique_together = (('user', 'group'),)
