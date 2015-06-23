from django.db import models
from datetime import date
#from django import forms

# Create your models here.
class Padre(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=255)
    apellido = models.CharField(null=False, max_length=255)
    correo = models.CharField(null=True, max_length=255)
    telefono = models.IntegerField(null=True, max_length=255)
    celular = models.IntegerField(null=True, max_length=255)
      
class Estudiante(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=255)
    apellido = models.CharField(null=False, max_length=255)
    correo = models.CharField(null=True, max_length=255)
    telefono = models.CharField(null=True, max_length=255)
    celular = models.CharField(null=True, max_length=255)
    padre = models.ForeignKey(Padre,null=True,related_name='Padre N/D')
    madre = models.ForeignKey(Padre,null=True,related_name='Madre N/D')
    color = models.IntegerField(null=True, max_length=255)
    estado_institucion = models.IntegerField(null=True, max_length=255) 
    
class Clase(models.Model):
    id = models.AutoField(primary_key=True, max_length=255)
    clave_materia = models.CharField(null=False, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    
class Grupo(models.Model):
    crn = models.IntegerField(primary_key=True,null=False, max_length=255)
    clase = models.ForeignKey(Clase, null=False)
    horario_1 = models.CharField(null=True, max_length=255)
    horario_2 = models.CharField(null=True, max_length=255)
    horario_3 = models.CharField(null=True, max_length=255)
    horario_4 = models.CharField(null=True, max_length=255)
    horario_5 = models.CharField(null=True, max_length=255)
    horario_6 = models.CharField(null=True, max_length=255)
    anio = models.IntegerField(null=True, max_length=255)
    semestre = models.IntegerField(null=True, max_length=255)
    profesor = models.CharField(null=False, max_length=255)
    
class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False)
    grupo = models.ForeignKey(Grupo, null=False)
    
class Antidoping(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=255)
    dia = models.CharField(default='', null=False, max_length=255)
    muestra_inicio = models.CharField(default='', null=False, max_length=255)
    muestra_fin = models.CharField(default='', null=False, max_length=255)
    antidoping_inicio = models.DateField(default=date.today)
    antidoping_fin = models.DateField(null=True,max_length=255)
    estado_antidoping = models.IntegerField(null=True, max_length=255)
    notas = models.CharField(null=False, max_length=255)
    
class EstudianteMuestra(models.Model):
    id = models.AutoField(primary_key=True)
    inscrito = models.ForeignKey(Inscrito,null=False)
    antidoping = models.ForeignKey(Antidoping,null=False)
    folio = models.CharField(null=False, max_length=255)
    tipo_seleccion = models.IntegerField(null=True, max_length=255)
    resultado = models.IntegerField(null=True, max_length=255)
    tipo_droga = models.CharField(null=True, max_length=255)
    estado = models.IntegerField(null=True, max_length=255)
    notas = models.CharField(null=True, max_length=255)
    respuestas = models.TextField(null=True)
