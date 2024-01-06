from django.contrib import admin
from .models import Board
from .models import SeaZone

# admin.site.register(Board)
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'board')


@admin.register(SeaZone)
class SeaZoneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SeaZone._meta.get_fields()]
    search_fields = ('sea_zone_name', )
