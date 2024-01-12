from django.contrib import admin
from game.models import ShipsLocalisations


@admin.register(ShipsLocalisations)
class ShipsLocalisationsAdmin(admin.ModelAdmin):
    """Ships Localisations on board for game."""

    list_display = [field.name for field in ShipsLocalisations._meta.get_fields()]
