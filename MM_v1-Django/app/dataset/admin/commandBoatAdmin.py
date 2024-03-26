from django.contrib import admin
from dataset.models import CommandBoatCard


@admin.register(CommandBoatCard)
class CommandBoatCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'boat',
        'boat_type',
        'expansion',
        'awers',
        'toughness',
        'cargo',
        'crew',
        'cannons',
        'maneuverability',
        'speed',
        'buy_cost',
        'sell_cost',
        'notes',
    ]
