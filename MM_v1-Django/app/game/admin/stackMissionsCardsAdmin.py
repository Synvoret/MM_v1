from django.contrib import admin
from game.models import StackMissionsCards


@admin.register(StackMissionsCards)
class StackMissionsCardsAdmin(admin.ModelAdmin):
    """Stack Missions Cards on board for game."""

    list_display = [
        'game_number',
        'mission_1_card',
        'mission_2_card',
        'mission_3_card',
    ]
