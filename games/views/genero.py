from django.shortcuts import render, redirect, get_object_or_404
from games.models import Game, Dev, Genero, Plat

def cria_genero(request):
    if request.method == 'POST':
        nome= request.POST ['nome']
        if not nome.strip():
            print('nome, nao pode ficarr em branco')
            return redirect('cria_genero')
        genero = Genero.objects.create(nome= nome)
        genero.save()
        return redirect('dashboard')
    else:
        return render(request, 'generos/cria_genero.html')