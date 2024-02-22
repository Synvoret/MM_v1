from django.contrib import admin
from game.models import TrackPlayerSpecialWeapons


@admin.register(TrackPlayerSpecialWeapons)
class TrackPlayerSpecialWeaponsAdmin(admin.ModelAdmin):
    """Ttack Player Special Weapons on board for game."""

    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
