from django.http import HttpResponse
from django.shortcuts import render
from AppPrimerEntrega.models import Especialista, Paciente, Tratamiento  
from AppPrimerEntrega.forms import FormularioPaciente, FormularioEspecialista, FormularioTratamiento, BusquedaPaciente
import random
# Create your views here.

# def nuevo_paciente(request):
#     DNI = random.randrange(1000000, 50000000)
#     paciente1 =  Paciente(nombre='Juan', apellido='Martinez', DNI=DNI, patologia='Alzheimer')
#     paciente1.save()
#     return HttpResponse(f"Se muestra la info de paciente {paciente1.nombre} {paciente1.apellido}")

# def entrega_formulario(request):
    
#     print(request.method)
#     if request.method == 'POST':
#         print(request.POST)
#         paciente_nuevo =  Paciente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], DNI=request.POST['DNI'], patologia=request.POST['patologia'])
#         paciente_nuevo.save()
#         return render(request, 'home/home.html', {'paciente_nuevo': paciente_nuevo})

    
#     return render(request, 'AppPrimerEntrega/entrega_formulario.html', {})

def formulario_paciente(request):
    
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], DNI=informacion['DNI'], patologia=informacion['patologia'])
            paciente.save()
            return render(request, 'home/home.html', {'paciente': paciente})
    formulario = FormularioPaciente()
    return render(request, 'AppPrimerEntrega/entrega_formulario.html', {'formulario': formulario})


def formulario_especialista(request):
    
    if request.method == 'POST':
        formulario = FormularioEspecialista(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            especialista = Especialista (nombre=informacion['nombre'], apellido=informacion['apellido'], especialidad=informacion['especialidad'], matricula=informacion['matricula'])
            especialista.save()
            return render(request, 'home/home.html', {'especialista': especialista})
    formulario = FormularioEspecialista()  
    return render(request, 'AppPrimerEntrega/entrega_formulario.html', {'formulario': formulario})

def formulario_tratamiento(request):
    
    if request.method == 'POST':
        formulario = FormularioTratamiento(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tratamiento = Tratamiento (fecha_inicio=informacion['fecha_inicio'], cura=informacion['cura'])
            tratamiento.save()
            return render(request, 'home/home.html', {'tratamiento': tratamiento})
    formulario = FormularioTratamiento()
    return render(request, 'AppPrimerEntrega/entrega_formulario.html', {'formulario': formulario})

def busqueda_paciente(request):
    pacientes_buscados = []
    dato = request.GET.get('partial_paciente', None)
    
    if dato is not None:
        pacientes_buscados = Paciente.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaPaciente()
    return render(request, 'AppPrimerEntrega/busqueda.html', {'buscador': buscador, 'pacientes_buscados': pacientes_buscados, 'dato': dato})