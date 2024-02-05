from django.contrib import admin
from game.models import TrackFavors


@admin.register(TrackFavors)
class TrackFavorsAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
