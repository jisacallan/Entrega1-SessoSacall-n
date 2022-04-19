from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from AppPrimerEntrega.models import Especialista, Paciente, Tratamiento  
from AppPrimerEntrega.forms import FormularioPaciente, FormularioEspecialista, FormularioTratamiento, BusquedaPaciente
from django.contrib.auth.decorators import login_required
# Create your views here.


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


@login_required
def formulario_especialista(request):
    
    if request.method == 'POST':
        formulario = FormularioEspecialista(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            especialista = Especialista (nombre=informacion['nombre'], apellido=informacion['apellido'], especialidad=informacion['especialidad'], matricula=informacion['matricula'], comentarios=informacion['comentarios'])
            especialista.save()
            return render(request, 'home/home.html', {'especialista': especialista})
    formulario = FormularioEspecialista()  
    return render(request, 'AppPrimerEntrega/entrega_formulario.html', {'formulario': formulario})

@login_required
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



#CRUD Básico: Pacientes

@login_required
def listado_paciente(request):
    listado_pacientes = Paciente.objects.all()
    return render(request, 'AppPrimerEntrega/listado_pacientes.html', {'listado_pacientes': listado_pacientes})


def crear_paciente(request):
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], DNI=informacion['DNI'], patologia=informacion['patologia'])
            paciente.save()
            return redirect('listado_paciente')
    formulario = FormularioPaciente()
    return render(request, 'AppPrimerEntrega/crear_paciente.html', {'formulario': formulario})


def actualizar_paciente(request, id):
    
    paciente = Paciente.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST)
        print(formulario)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente.nombre = informacion['nombre']
            paciente.apellido = informacion['apellido']
            paciente.DNI = informacion['DNI']
            paciente.patologia = informacion['patologia']
            paciente.save()
            return redirect('listado_paciente')
    
    formulario = FormularioPaciente(initial={
        'nombre': paciente.nombre,
        'apellido': paciente.apellido,
        'DNI': paciente.DNI,
        'patologia': paciente.patologia 
    })
    return render(request, 'AppPrimerEntrega/actualizar_paciente.html', {'formulario': formulario, 'paciente': paciente})


def borrar_paciente(request, id):
    
    paciente = Paciente.objects.get(id=id)
    paciente.delete()    
    return redirect('listado_paciente')


@login_required
def busqueda_paciente(request):
    pacientes_buscados = []
    dato = request.GET.get('partial_paciente', None)
    
    if dato is not None:
        pacientes_buscados = Paciente.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaPaciente()
    return render(request, 'AppPrimerEntrega/busqueda.html', {'buscador': buscador, 'pacientes_buscados': pacientes_buscados, 'dato': dato})


#CRUD especialista (con CBV)


class EspecialistaLista(ListView):
    model = Especialista
    template_name = 'AppPrimerEntrega/listado_especialistas.html'

    
class EspecialistaDetalle(DetailView):
    model = Especialista
    template_name = 'AppPrimerEntrega/datos_especialistas.html'

    
class EspecialistaEditar(UpdateView):
    model = Especialista
    success_url = '/AppPrimerEntrega/especialistas/lista'
    fields = ['nombre', 'apellido', 'especialidad', 'matricula', 'comentarios']

    
class EspecialistaBorrar(DeleteView):
    model = Especialista
    success_url = '/AppPrimerEntrega/especialistas/lista'