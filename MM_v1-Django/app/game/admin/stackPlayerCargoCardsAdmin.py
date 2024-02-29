from django.contrib import admin
from game.models import StackPlayerCargoCards


@admin.register(StackPlayerCargoCards)
class StackPlayerCargoCardsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'player_colour',
        'cargo_card_1',
        'cargo_card_2',
        'cargo_card_3',
        'cargo_card_4',
        'cargo_card_5',
        'cargo_card_6',
        'cargo_card_7',
        'cargo_card_8',
    ]
