from django.urls import path
from . views import nuevo_paciente, entrega_formulario

urlpatterns = [
    path('nuevo', nuevo_paciente, name='nuevo_paciente'),
    path('formulario', entrega_formulario, name='entrega_formulario')
]
