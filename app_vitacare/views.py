from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario

def index(request):
    return render(request,'usuarios/index.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona após login bem-sucedido
        else:
            messages.error(request, 'Email ou senha incorretos.')  # Mostra mensagem de erro
            return redirect('login')  # Volta para a página de login

    return render(request, 'usuarios/login.html')

def register(request):
  if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])  
            usuario.save()
            return redirect('login')  
        else:
            form = UsuarioForm()

        return render(request, 'usuarios/register.html', {'form': form})

def consultas(request):
  return render(request, 'usuarios/consultas.html')
