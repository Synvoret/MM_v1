from django.contrib import admin
from game.models import StackEventsNPCCaptains


@admin.register(StackEventsNPCCaptains)
class StackEventsNPCCaptainsAdmin(admin.ModelAdmin):
    """Stack Events NPC Captains cards on board for game."""

    list_display = [
        "game_number",

        "captain",
        'nationality',
        'ship',
    ]
