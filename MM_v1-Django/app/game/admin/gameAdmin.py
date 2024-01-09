from django.contrib import admin
from game.models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Game Admin model."""

    list_display = [
        'number', 
        'round',
        'amount_players',
    ]
