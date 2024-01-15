from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BitacoraActividad(models.Model):
    bit_id = models.AutoField(primary_key=True)
    bit_descripcionactividad = models.TextField(blank=True, null=True)
    bit_fechahoraactividaddia = models.IntegerField(blank=True, null=True)
    bit_fechahoraactividadmes = models.IntegerField(blank=True, null=True)
    bit_fechahoraactividadanio = models.IntegerField(blank=True, null=True)
    usr = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    bit_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora_actividad'


class Contrato(models.Model):
    con_id = models.AutoField(primary_key=True)
    cli = models.ForeignKey('MaeCliente', models.DO_NOTHING, blank=True, null=True)
    con_fechainiciodia = models.IntegerField(blank=True, null=True)
    con_fechainiciomes = models.IntegerField(blank=True, null=True)
    con_fechainicioanio = models.IntegerField(blank=True, null=True)
    con_fechavencdia = models.IntegerField(blank=True, null=True)
    con_fechavencmes = models.IntegerField(blank=True, null=True)
    con_fechavencanio = models.IntegerField(blank=True, null=True)
    con_tipocontrato = models.CharField(max_length=100, blank=True, null=True)
    con_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'


class MaeCliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nombreempresa = models.CharField(max_length=255, blank=True, null=True)
    cli_infocontacto = models.CharField(max_length=255, blank=True, null=True)
    cli_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mae_cliente'


class ReqMantenimiento(models.Model):
    req_id = models.AutoField(primary_key=True)
    req_descripcion = models.TextField(blank=True, null=True)
    req_fechasolicituddia = models.IntegerField(blank=True, null=True)
    req_fechasolicitudmes = models.IntegerField(blank=True, null=True)
    req_fechasolicitudanio = models.IntegerField(blank=True, null=True)
    req_estado = models.CharField(max_length=100, blank=True, null=True)
    con = models.ForeignKey(Contrato, models.DO_NOTHING, blank=True, null=True)
    usuarioresponsable = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    req_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_mantenimiento'


class RolUsuario(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombrerol = models.CharField(max_length=100, blank=True, null=True)
    rol_descripcion = models.TextField(blank=True, null=True)
    rol_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol_usuario'


class Usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_nombreusuario = models.CharField(max_length=100, blank=True, null=True)
    usr_apellidousuario = models.CharField(max_length=100, blank=True, null=True)
    
    #usr_contrasenaencriptada = models.CharField(max_length=255, blank=True, null=True)
    
    usr_dni = models.CharField(max_length=8, blank=True, null=True)
    usr_celular = models.CharField(max_length=20, blank=True, null=True)
    rolusuario = models.ForeignKey(RolUsuario, models.DO_NOTHING, blank=True, null=True)
    usr_estadoregistro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'usuario'