from django.contrib import admin
from game.models import TrackPlayerHitLocations


@admin.register(TrackPlayerHitLocations)
class TrackPlayerHitLocationsAdmin(admin.ModelAdmin):
    """Ttack Player Hit Locations on board for game."""

    list_display = [
        'game_number',
        'game_round',
        'player_colour',

        'hull',
        'cargo',
        'masts',
        'crew',
        'cannons'
    ]
