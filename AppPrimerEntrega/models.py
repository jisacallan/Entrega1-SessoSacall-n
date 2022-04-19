from django.db import models
from ckeditor.fields import RichTextField

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
    comentarios = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f"Datos del especialista {self.nombre} {self.apellido}, {self.especialidad} matrícula {self.matricula}"
    
class Tratamiento(models.Model):
    fecha_inicio = models.DateTimeField()
    cura = models.BooleanField()
    
    def __str__(self):
        return f"El tratamiento inicia en {self.fecha_inicio}"