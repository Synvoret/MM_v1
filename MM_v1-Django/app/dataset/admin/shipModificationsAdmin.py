from django.contrib import admin
from dataset.models import ShipModifications


@admin.register(ShipModifications)
class ShipModificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'awers', 'rewers')
