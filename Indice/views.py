from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreado, UserEditar
from django.contrib.auth.decorators import login_required
from .models import UserAvatar

# Create your views here.

@login_required
def home(request):
    return render(request, "home/home.html", {'user_avatar_url': url_avatar(request.user)})


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return render(request, 'home/home.html', {'msj': 'Ingreso correcto'})
            
            else:
                return render(request, 'home/login.html', {'form': form, 'msj': 'No se autenticó'})
            
        else:
            return render(request, 'home/login.html', {'form': form, 'msj': 'Datos incorrectos'})
        
    else:
        form = AuthenticationForm()
        return render(request, "home/login.html", {'form': form, 'msj': ''})
    

def registrar(request):
    
    if request.method == 'POST':
        form = UserCreado(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home/home.html', {'msj': f'Se creo el usuario {username} correctamente'})
        else:
            return render(request, 'home/registrar.html', {'form': form, 'msj': ''})
    
    form = UserCreado()
    return render(request, 'home/registrar.html', {'form': form, 'msj': ''})


@login_required
def editar(request):
    msj = ''
    
    if request.method == 'POST':
        form = UserEditar(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj = 'La contraseña no ha sido modificada.'
            
            logued_user.save()
            
            return render(request, 'home/home.html', {'msj': msj, 'user_avatar_url': url_avatar(request.user)})
        else:
            return render(request, 'home/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': url_avatar(request.user)})
           
    form = UserEditar(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email, 'username': request.user.username})
    return render(request, 'home/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': url_avatar(request.user)})


def url_avatar(user):
    return UserAvatar.objects.filter(user=user)[0].imagen.url


@login_required
def editar_usuario(request):
    
    user_extension_logued, _ = UserAvatar.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserEditar(request.POST, request.FILES)
        
        if form.is_valid():
            
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('index')
        else:
            return render(request, 'home/editar_usuario.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = UserEditar(
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'home/editar_usuario.html', {'form': form})

@login_required
def usuario_datos(request):
    return render(request, 'home/usuario_datos.html', {})