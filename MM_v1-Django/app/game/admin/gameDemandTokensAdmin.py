from django.contrib import admin
from game.models import GameDemandTokens


@admin.register(GameDemandTokens)
class GameDemandTokensAdmin(admin.ModelAdmin):
    """Admin Demands Tokens for Game."""

    list_display = [
        'game_number',
        'game_round',

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
