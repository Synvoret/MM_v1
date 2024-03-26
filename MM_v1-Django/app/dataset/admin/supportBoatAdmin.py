from django.contrib import admin
from dataset.models import SupportBoatCard


@admin.register(SupportBoatCard)
class SupportBoatCardAdmin(admin.ModelAdmin):
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
        'seamanship',
        'leadership',
        'buy_cost',
        'sell_cost',
        'notes',
    ]
