from django.contrib import admin
from .models import CombatFlowDiagram

# admin.site.register()
@admin.register(CombatFlowDiagram)
class CombatFlowDiagramAdmin(admin.ModelAdmin):
    list_display = ('name', 'diagram')
