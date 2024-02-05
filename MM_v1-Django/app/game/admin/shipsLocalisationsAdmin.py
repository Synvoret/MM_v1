from django.contrib import admin
from game.models import ShipsLocalisations


@admin.register(ShipsLocalisations)
class ShipsLocalisationsAdmin(admin.ModelAdmin):
    """Ships Localisations on board for game."""

    # list_display = [field.name for field in ShipsLocalisations._meta.get_fields()]
    list_display = [
        'game_number',
        'blue_ship',
        'blue_in_port',
        'green_ship',
        'green_in_port',
        'red_ship',
        'red_in_port',
        'yellow_ship',
        'yellow_in_port',
        'merchants_ship',
        'dutch_ship',
        'english_ship',
        'french_ship',
        'spanish_ship',
        'small_pirate_ship',
        'large_pirate_ship',
    ]
