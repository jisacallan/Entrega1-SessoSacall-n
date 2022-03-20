from django.contrib import admin
from . models import Especialista, Paciente, Tratamiento

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Especialista)
admin.site.register(Tratamiento)