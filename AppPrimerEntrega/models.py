from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    DNI = models.IntegerField()
    patologia = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Datos del paciente {self.nombre} {self.apellido}, DNI {self.DNI} con patología {self.patologia}"
    
class Especialista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)
    matricula = models.IntegerField(default=None)
    
class Tratamiento(models.Model):
    fecha_inicio = models.DateTimeField()
    cura = models.BooleanField()