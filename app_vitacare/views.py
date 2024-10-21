from django.shortcuts import render, redirect
from .forms import UsuarioForm

def index(request):
    return render(request,'usuarios/index.html')

def user_login(request):
    return render(request, 'usuarios/login.html')

def register(request):
  if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = form.cleaned_data['senha']  # Aqui você pode adicionar criptografia da senha, se desejar.
            usuario.save()
            return redirect('login')  
        else:
            form = UsuarioForm()
        return render(request, 'usuarios/register.html', {'form': form})


def consultas(request):
  return render(request, 'usuarios/consultas.html')
