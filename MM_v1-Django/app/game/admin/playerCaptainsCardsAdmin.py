from django.contrib import admin
from game.models import PlayersCaptainsCards


@admin.register(PlayersCaptainsCards)
class PlayersCaptainsCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',
        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
