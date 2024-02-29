from django.contrib import admin
from game.models import TrackPlayersShipModifications


@admin.register(TrackPlayersShipModifications)
class TrackPlayersShipModificationsAdmin(admin.ModelAdmin):
    """Ttack Player Ship Modifications on board for game."""

    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
