from django.shortcuts import render, redirect, get_object_or_404
from games.models import Game, Dev, Genero, Plat

def cria_desenvolvedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        if not nome.strip():
            print('nome, nao pode ficarr em branco')
            return redirect('cria_desenvolvedor')
        endereco = request.POST['endereco']
        if not endereco.strip():
            print('endereco, nao pode ficarr em branco')
            return redirect('cria_desenvolvedor')
        dev = Dev.objects.create(nome=nome, endereco=endereco)
        dev.save()
        return redirect('dashboard')
    else:
        return render(request, 'desenvolvedores/cria_desenvolvedor.html')