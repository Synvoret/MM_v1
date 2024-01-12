from django.contrib import admin
from .models import Game
from .models import StackEventsCards


admin.site.register(Game)


@admin.register(StackEventsCards)
class StackEventsCardsAdmin(admin.ModelAdmin):
    """Stack Events Cards on board for game."""

    list_display = [
        'game',
        'game_round',
        'event_card',
    ]
