from django.contrib import admin
from game.models import TrackGloryPoint


@admin.register(TrackGloryPoint)
class TrackGloryPointAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
