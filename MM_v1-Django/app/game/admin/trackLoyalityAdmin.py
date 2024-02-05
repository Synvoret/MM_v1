from django.contrib import admin
from game.models import TrackLoyality


@admin.register(TrackLoyality)
class TrackLoyalityAdmin(admin.ModelAdmin):
    list_display = [
        'game_number',

        'player_blue',
        'player_green',
        'player_red',
        'player_yellow',
    ]
