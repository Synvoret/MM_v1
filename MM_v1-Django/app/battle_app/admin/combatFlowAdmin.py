# OLD
# # from django.contrib import admin
# from battle_app.models import CombatFlow


# @admin.register(CombatFlow)
# class CombatFlowAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in CombatFlow._meta.fields if field.name != 'id']



# NEW
from django.contrib import admin
from django.utils.html import format_html
import json
from battle_app.models import CombatFlow

@admin.register(CombatFlow)
class CombatFlowAdmin(admin.ModelAdmin):
    # Wykluczamy oryginalne pole 'combat' i dodajemy własną metodę
    list_display = [field.name for field in CombatFlow._meta.fields if field.name not in ('id', 'combat')] + ['formatted_combat']

    def formatted_combat(self, obj):
        if obj.combat:
            formatted_data = json.dumps(obj.combat, indent=1)
            return format_html("<pre>{}</pre>", formatted_data)
        return "-"
    formatted_combat.short_description = "Combat"
