from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = form.save()
            # Iniciar sesión automáticamente después de registrar al usuario
            login(request, user)
            # Mostrar mensaje de éxito
            messages.success(request, '¡Te has registrado exitosamente!')
            return redirect('index')  # Redirigir a la página de inicio o donde lo necesites
        else:
            # Si el formulario no es válido, renderizamos la página con los errores
            return render(request, 'accounts/register.html', {'form': form})
    else:
        # Si es una solicitud GET, solo mostramos el formulario vacío
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito!')
            return redirect('login')  # Redirigir al login después del registro exitoso
        else:
            messages.error(request, 'Error al crear la cuenta. Por favor, inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# Inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige al usuario a la página de inicio
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

# Cierre de sesión
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión.')
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Obtener el usuario con el formulario válido
            user = form.get_user()
            # Autenticar y loguear al usuario
            login(request, user)
            # Mensaje de éxito (opcional)
            messages.success(request, 'Has iniciado sesión correctamente.')
            # Redirigir al usuario a la página principal o cualquier página que desees
            return redirect('index')  # O a la página que desees
        else:
            # Si el formulario no es válido, se muestra el formulario con los errores
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()  # Formulario vacío para GET

    return render(request, 'accounts/login.html', {'form': form})