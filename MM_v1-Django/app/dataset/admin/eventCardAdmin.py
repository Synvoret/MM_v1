from django.contrib import admin
from dataset.models import EventCard


@admin.register(EventCard)
class EventCardAdmin(admin.ModelAdmin):
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',
        'moving',
        'dutch_direction',
        'english_direction',
        'french_direction',
        'spanish_direction',
        'large_pirate_direction',
        'small_pirate_direction',
        'nationality',
        'sea_zone_start',
        'ship',
        'npc_name',
        'seamanship',
        'scouting',
        'leadership',
        'reward',
        'notes',
    ]