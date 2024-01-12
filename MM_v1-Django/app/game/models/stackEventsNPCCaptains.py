from django.db import models
from .game import Game
from dataset.models import EventCard


class StackEventsNPCCaptains(models.Model):
    """Presents a stack for all Events NPC Captains cards on board."""

    def captain_name(self):
        try:
            # Assuming large_pirate is a ForeignKey to EventCard model
            return self.captain.npc_name
        except EventCard.DoesNotExist:
            return None

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    captain = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Stack NPC Captains cards for game - {self.game_number}"
