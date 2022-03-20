from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    DNI = models.IntegerField()
    patologia = models.CharField(max_length=50)
    
class Especialista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)
    matricula = models.IntegerField()
    
class Tratamiento(models.Model):
    fecha_inicio = models.DateTimeField()
    cura = models.BooleanField()