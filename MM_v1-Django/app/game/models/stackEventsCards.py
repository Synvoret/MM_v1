from django.db import models
from .game import Game
from dataset.models import EventCard


class StackEventsCards(models.Model):
    """Presents a stack for events cards in board"""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    event_card = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)
    event_card_captain = models.BooleanField(default=False)

    def __str__(self):
        return f"Stack events card."
