from django.contrib import admin
from dataset.models import Ship


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'colour', 'image']
