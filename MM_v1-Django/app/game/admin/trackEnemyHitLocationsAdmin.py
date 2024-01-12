from django.contrib import admin
from game.models import TrackEnemyHitLocations


@admin.register(TrackEnemyHitLocations)
class TrackEnemyHitLocationsAdmin(admin.ModelAdmin):
    """Ttack Enemy Hit Locations on board for game."""

    list_display = [
        'game_number',

        'hull',
        'cargo',
        'masts',
        'crew',
        'cannons'
    ]
