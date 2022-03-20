from django.urls import path
from . views import nuevo_paciente

urlpatterns = [
    path('nuevo', nuevo_paciente, name='nuevo_paciente'),
]
