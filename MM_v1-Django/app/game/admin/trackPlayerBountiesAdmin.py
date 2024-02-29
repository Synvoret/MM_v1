from django.contrib import admin
from game.models import TrackPlayerBounties


@admin.register(TrackPlayerBounties)
class TrackPlayerBountiesAdmin(admin.ModelAdmin):
    """Ttack Player Bounties on board for game."""

    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
