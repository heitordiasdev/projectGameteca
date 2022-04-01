from django.shortcuts import render, redirect, get_object_or_404
from games.models import Game, Dev, Genero, Plat

def cria_plataforma(request):
    if request.method == 'POST':
        nome= request.POST ['nome']
        if not nome.strip():
            print('nome, nao pode ficarr em branco')
            return redirect('cria_plataforma')
        plat = Plat.objects.create(nome= nome)
        plat.save()
        return redirect('dashboard')
    else:
        return render(request, 'plataformas/cria_plataforma.html')