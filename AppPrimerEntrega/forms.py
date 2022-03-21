from django import forms

class FormularioPaciente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    DNI = forms.IntegerField()
    patologia = forms.CharField(max_length=50)

class FormularioEspecialista(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    especialidad = forms.CharField(max_length=20)
    matricula = forms.IntegerField()
    
class FormularioTratamiento(forms.Form):
    fecha_inicio = forms.DateTimeField()
    cura = forms.BooleanField(required=False)
    
class BusquedaPaciente(forms.Form):
    partial_paciente = forms.CharField(label='Buscador de pacientes' ,max_length=20)