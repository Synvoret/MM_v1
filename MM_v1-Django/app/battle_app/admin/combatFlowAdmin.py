from django.contrib import admin
from battle_app.models import CombatFlow


@admin.register(CombatFlow)
class CombatFlowAdmin(admin.ModelAdmin):
    # list_display = [
    #     'aggressor',
    #     'defender',
    #     "round",
    #     "aggressor_seamanship",

    #     ]
    list_display = [field.name for field in CombatFlow._meta.fields if field.name != 'id']
