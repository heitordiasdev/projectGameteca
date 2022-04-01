from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from games.models import Game, Dev, Genero, Plat
from django.contrib import messages


def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if not nome.strip():
            print('O campo não pode ficar em branco!')
            return redirect('cadastro')
        if not email.strip():
            print('O campo não pode ficar em branco!')
            return redirect('cadastro')
        if not senha1.strip():
            print('O campo não pode ficar em branco!')
            return redirect('cadastro')

        if senha1 != senha2:
            messages.error(request, 'Senhas tem que ser iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já cadastrado!')
            return redirect('cadastro')
        usuario = User.objects.create_user(username=nome, email=email, password=senha1)
        usuario.save()
        messages.success(request, 'Usuario cadastrado com sucesso!')

        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if senha.strip() == '':
            messages.error(request, 'os campos email e/ou senha não podem ficar em branco!')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario= auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Email e/ou senha incorreto(s)!')
        else:
            messages.error(request, 'Email e/ou senha incorreto(s)!')
    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        games = Game.objects.filter(usuario= id)
        dados = {
            'games': games
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


