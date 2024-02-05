from django.contrib import admin
from game.models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Game Admin model."""

    list_display = [
        'number',
        'rounds',
        'amount_players',
        'player_blue_play',
        'player_blue_done',
        'player_green_play',
        'player_green_done',
        'player_red_play',
        'player_red_done',
        'player_yellow_play',
        'player_yellow_done',
        ]
