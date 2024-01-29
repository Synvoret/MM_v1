from django.contrib import admin
from dataset.models import FishingCard


@admin.register(FishingCard)
class FishingCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'fishing_value',
        'fishing_hits',
        'notes',
    ]
