from django.urls import path
from . views import formulario_paciente, formulario_especialista, formulario_tratamiento, busqueda_paciente

urlpatterns = [
    path('paciente', formulario_paciente, name='formulario_paciente'),
    path('especialista', formulario_especialista, name='formulario_especialista'),
    path('tratamiento', formulario_tratamiento, name='tratamiento'),
    path('busqueda-paciente', busqueda_paciente, name='busqueda_paciente')
]
