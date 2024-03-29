from django.contrib import admin
from dataset.models import ShipCard


@admin.register(ShipCard)
class ShipCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'ship',
        'ship_type',
        'expansion',
        'awers',
        'toughness',
        'cargo',
        'crew',
        'cannons',
        'maneuverability',
        'speed',
        'boats',
        'buy_cost',
        'sell_cost',
        'notes',
    ]
