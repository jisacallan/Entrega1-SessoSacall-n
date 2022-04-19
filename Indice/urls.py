from django.urls import path
from . views import home, login, registrar, editar, editar_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('login/', login ,name='login'),
    path('logout/', LogoutView.as_view(template_name='home/home.html') ,name='logout'),
    path('registrar/', registrar ,name='registrar'),
    path('editar/', editar, name='editar'),
    path('editar/usuario/', editar_usuario, name='editar_usuario'),
]
