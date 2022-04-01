from django.contrib import admin
from .models import Dev, Genero, Plat, Game

class listDev(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5

class listPlat(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5

class listGames(admin.ModelAdmin):
    list_display = ('id', 'nome', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('dev',)
    list_editable = ('publicado',)

    list_per_page = 5

admin.site.register(Dev, listDev)
admin.site.register(Genero)
admin.site.register(Plat, listPlat)
admin.site.register(Game, listGames)

