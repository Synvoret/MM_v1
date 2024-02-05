from django.db import models
from .game import Game
from dataset.models import MissionCard


class StackMissionsCards(models.Model):
    """Presents a stack for missions cards in board"""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    mission_1_card = models.ForeignKey(MissionCard, on_delete=models.CASCADE, related_name='mission_1', null=True, blank=True)
    mission_2_card = models.ForeignKey(MissionCard, on_delete=models.CASCADE, related_name='mission_2', null=True, blank=True)
    mission_3_card = models.ForeignKey(MissionCard, on_delete=models.CASCADE, related_name='mission_3', null=True, blank=True)

    def __str__(self):
        return f"Stack missions card."
