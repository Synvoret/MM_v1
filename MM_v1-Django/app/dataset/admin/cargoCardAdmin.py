from django.contrib import admin
from dataset.models import CargoCard


@admin.register(CargoCard)
class CargoCardAdmin(admin.ModelAdmin):
    
    # list_display = [field.name for field in CargoCard._meta.get_fields()]
    list_display = [
        'deck',
        'card',
        'expansion',
        'awers',

        'cargo',
        'contraband_text',
        'contraband_destination',
        'plunder_value',
        'hits',

        'notes',
        ]
