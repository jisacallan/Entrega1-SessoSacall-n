from django.urls import path
# from . views import formulario_paciente, busqueda_paciente, listado_paciente, borrar_paciente, crear_paciente, actualizar_paciente, formulario_especialista, crear_especialista, formulario_tratamiento
from . import views


urlpatterns = [
    # path('paciente', views.formulario_paciente, name='formulario_paciente'),
    path('busqueda-paciente', views.busqueda_paciente, name='busqueda_paciente'),
    path('paciente/listado', views.listado_paciente, name='listado_paciente'),
    path('crear-paciente', views.crear_paciente, name='crear_paciente'),
    path('borrar-paciente/<int:id>/', views.borrar_paciente, name='borrar_paciente'),
    path('actualizar-paciente/<int:id>/', views.actualizar_paciente, name='actualizar_paciente'),
    
    path('especialista', views.formulario_especialista, name='formulario_especialista'),
    # path('especialista/listado', views.listado_especialista, name='listado_especialista'),
    # path('crear-especialista', views.crear_especialista, name='crear_especialista'),
    # path('borrar-especialista', views.borrar_especialista, name='borrar_especialista'),
    # path('actualizar-especialista', views.actualizar_especialista, name='actualizar_especialista'),
    path('especialistas/lista', views.EspecialistaLista.as_view(), name='especialistas_listado'),
    path('especialistas/<int:pk>', views.EspecialistaDetalle.as_view(), name='especialistas_detalle'),
    # path(r'^/(?P<pk>\d+)$', views.EspecialistaDetalle.as_view(), name='especialistas_detalle'),
    path('especialistas/<int:pk>/editar', views.EspecialistaEditar.as_view(), name='especialistas_editar'),
    path('especialistas/<int:pk>/borrar', views.EspecialistaBorrar.as_view(), name='especialistas_borrar'),

    path('tratamiento', views.formulario_tratamiento, name='tratamiento'),    
]
