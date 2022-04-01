from django.shortcuts import render, get_object_or_404, redirect
from games.models import Game, Dev, Genero, Plat
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    games = Game.objects.filter(publicado=True)
    dados = {
        'games' : games
    }
    return render(request, 'index.html', dados)

def games(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game_a_exibir = {
        'game': game
    }
    return render(request, 'games.html', game_a_exibir)

def buscar(request):
    lista_games = Game.objects.filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar= request.GET['buscar']
        if nome_a_buscar:
            lista_games = lista_games.filter(nome__icontains=nome_a_buscar)

    dados = {
        'games': lista_games
    }
    return render(request, 'buscar.html', dados)

def cria_games(request):
    desenvolvedores = Dev.objects.all()
    generos = Genero.objects.all()
    plataformas = Plat.objects.all()

    dados = {
        'desenvolvedores': desenvolvedores,
        'generos': generos,
        'plataformas': plataformas
    }

    if request.method == 'POST':
        usuario = get_object_or_404(User, pk=request.user.id)
        nome =  request.POST['nome']
        data_lanc = request.POST['data_lanc']
        generos_id = request.POST['genero']
        lista_gen = []
        for id in generos_id:
            gen = get_object_or_404(Genero, pk=id)
            lista_gen.append(gen)
        plataformas_id = request.POST['plataforma']
        lista_plat = []
        for id in plataformas_id:
            plat = get_object_or_404(Plat, pk=id)
            lista_plat.append(plat)
        enredo = request.POST['enredo']
        critica = request.POST['critica']
        avaliacao = request.POST['avaliacao']
        desenvolvedores_id = request.POST.getlist('dev')
        lista_dev = []
        for id in desenvolvedores_id:
            Desv = get_object_or_404(Dev, pk=id)
            lista_dev.append(Desv)
        capa_game = request.FILES['capa_game']
        game = Game.objects.create(usuario= usuario, nome= nome, data_lanc= data_lanc, enredo= enredo,
                                   critica=critica, avaliacao= avaliacao,
                                   capa_game= capa_game)

        game.genero.set(lista_gen)
        game.plataforma.set(lista_plat)
        game.dev.set(lista_dev)
        game.save()
        messages.success(request, 'o game foi cadastrado com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'games/cria_games.html', dados)

def deleta_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'o game foi removido com sucesso!')
    return redirect('dashboard')

def edita_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    desenvolvedores = Dev.objects.all()
    generos = Genero.objects.all()
    plataformas = Plat.objects.all()

    dados = {
        'desenvolvedores': desenvolvedores,
        'generos': generos,
        'plataformas': plataformas,
        'game': game
    }

    return render(request, 'games/edita_game.html', dados)

def atualiza_game(request):
    if request.method == 'POST':
        game_id= request.POST['game_id']
        g = get_object_or_404(Game, pk=game_id)
        g.nome = request.POST['nome']
        g.data_lanc = request.POST['data_lanc']
        generos_id = request.POST['genero']
        lista_gen = []
        for id in generos_id:
            gen = get_object_or_404(Genero, pk=id)
            lista_gen.append(gen)
        plataformas_id = request.POST['plataforma']
        lista_plat = []
        for id in plataformas_id:
            plat = get_object_or_404(Plat, pk=id)
            lista_plat.append(plat)
        g.enredo = request.POST['enredo']
        g.critica = request.POST['critica']
        g.avaliacao = request.POST['avaliacao']
        desenvolvedores_id = request.POST.getlist('dev')
        lista_dev = []
        for id in desenvolvedores_id:
            Desv = get_object_or_404(Dev, pk=id)
            lista_dev.append(Desv)
        g.genero.set(lista_gen)
        g.plataforma.set(lista_plat)
        g.dev.set(lista_dev)
        if 'capa_game' in request.FILES:
            g.capa_game = request.FILES['capa_game']

        g.save()
        messages.success(request, 'o game foi atualizado com sucesso!')
        return redirect('dashboard')



