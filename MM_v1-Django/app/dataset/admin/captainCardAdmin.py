from django.contrib import admin
from dataset.models import CaptainCard


@admin.register(CaptainCard)
class CaptainCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'captain',
        'expansion',
        'awers',
        'home_port',
        'nationality',
        'seamanship',
        'scouting',
        'leadership',
        'influence',
        'notes',
    ]
