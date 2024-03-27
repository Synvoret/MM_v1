from django.contrib import admin
from game.models import GamePorts


@admin.register(GamePorts)
class GamePortsAdmin(admin.ModelAdmin):
    list_display = (
        'game_number',
        )
