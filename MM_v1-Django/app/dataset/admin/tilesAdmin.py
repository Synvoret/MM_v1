from django.contrib import admin
from dataset.models import Tile


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
