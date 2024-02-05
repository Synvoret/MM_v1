from django.contrib import admin
from game.models import GameShipModifications


@admin.register(GameShipModifications)
class GameShipModificationsAdmin(admin.ModelAdmin):
    """Admin Ship Modifications for Game."""

    list_display = [
        'game_number',

        'basse_terre',
        'bridgetown',
        'caracas',
        'cartagena',
        'curacao',
        'gulf_city',
        'nassau',
        'havana',
        'old_providence',
        'petite_goave',
        'port_royal',
        'san_juan',
        'santo_domingo',
        'st_john',
        'st_maarten',
        'trinidad',
        'tortuga',
    ]
