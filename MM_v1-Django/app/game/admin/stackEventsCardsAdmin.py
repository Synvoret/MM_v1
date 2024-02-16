from django.contrib import admin
from game.models import StackEventsCards


@admin.register(StackEventsCards)
class StackEventsCardsAdmin(admin.ModelAdmin):
    """Stack Events Cards on board for game."""

    list_display = [
        'game_number',
        'game_round',
        'event_card',
        'event_card_captain',
    ]
