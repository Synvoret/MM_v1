from django.contrib import admin
from dataset.models import PortCard

@admin.register(PortCard)
class PortCardAdmin(admin.ModelAdmin):
    """Game Ports Admin model."""

    list_display = [
        'deck',
        'sea_zone',
        'image',
        'expansion',
        'nationality',
        'fortitude',
        'stockpile',
        'soldiers',
        'cannons',
        'defensibility',
        'boats',
        ]
