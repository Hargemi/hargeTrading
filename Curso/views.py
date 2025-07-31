from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

def inicio(request):   
    return render(request, 'Curso/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Bienvenido! Has iniciado sesión correctamente.')
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'Curso/login.html')

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'Curso/registro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'Curso/registro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'Curso/registro.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'Curso/registro.html')

def logout_view(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión correctamente!')
    return redirect('inicio')