from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'usuarios/index.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        usuario = authenticate(request, email=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('consultas')  # Redireciona para a página de consultas
        else:
            messages.error(request, 'Email ou senha incorretos')
            return render(request, 'usuarios/login.html')
    return render(request, 'usuarios/login.html')

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])  
            usuario.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UsuarioForm()  # Inicializa o formulário vazio em caso de GET ou erro

    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def consultas(request):
  return render(request, 'usuarios/consultas.html')
