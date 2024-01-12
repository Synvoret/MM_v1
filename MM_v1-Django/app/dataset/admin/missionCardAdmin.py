from django.contrib import admin
from dataset.models import MissionCard


@admin.register(MissionCard)
class MissionCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'earn',
        'requirements',
        'port',
        'notes'
    ]
