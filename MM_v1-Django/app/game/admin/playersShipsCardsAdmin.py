from django.contrib import admin
from game.models import PlayersShipsCards


@admin.register(PlayersShipsCards)
class PlayersShipsCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
