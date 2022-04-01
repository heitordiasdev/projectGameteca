from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:game_id>', games, name='games'),
    path('buscar', buscar, name= 'buscar'),
    path('cria/games', cria_games, name= 'cria_games'),
    path('deleta/<int:game_id>', deleta_game, name='deleta_game'),
    path('edita/<int:game_id>', edita_game, name='edita_game'),
    path('atualiza_game', atualiza_game, name= 'atualiza_game'),
    path('cria/desenvolvedor', cria_desenvolvedor, name='cria_desenvolvedor'),
    path('cria/genero', cria_genero, name= 'cria_genero'),
    path('cria/plataforma', cria_plataforma, name= 'cria_plataforma')

]