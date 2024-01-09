from django.contrib import admin
from game.models import PlayersGloryCards


@admin.register(PlayersGloryCards)
class PlayersGloryCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',
        'game_round',

        'player_colour',
        'glory_card_1',
        'glory_card_2',
        'glory_card_3',
        'glory_card_4',
        'glory_card_5',
        'glory_card_6',
    ]
