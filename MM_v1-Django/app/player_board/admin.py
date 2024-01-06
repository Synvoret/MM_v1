from django.contrib import admin
from .models import PlayerBoard


@admin.register(PlayerBoard)
class PlayerBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'player_board_image')
