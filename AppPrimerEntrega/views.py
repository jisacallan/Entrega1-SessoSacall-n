from django.http import HttpResponse
from django.shortcuts import render
from AppPrimerEntrega.models import Paciente  
import random
# Create your views here.

def nuevo_paciente(request):
    DNI = random.randrange(1000000, 50000000)
    paciente1 =  Paciente(nombre='Juan', apellido='Martinez', DNI=DNI, patologia='Alzheimer')
    paciente1.save()
    return HttpResponse(f"Se muestra la info de paciente {paciente1.nombre} {paciente1.apellido}")

def entrega_formulario(request):
    return render(request, 'AppPrimerEntrega/entrega_formulario.html', {})