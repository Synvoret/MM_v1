from django.contrib import admin
from dataset.models import GloryCard


@admin.register(GloryCard)
class GloryCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'notes',
    ]
