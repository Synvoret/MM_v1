from django.db import models
from .game import Game


class TrackEnemyHitLocations(models.Model):
    """Presents a track for enemy hit locations values."""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    hull = models.IntegerField(default=1)
    cargo = models.IntegerField(default=1)
    masts = models.IntegerField(default=1)
    crew = models.IntegerField(default=1)
    cannons = models.IntegerField(default=1)

    def __str__(self):
        return f"Track Enemy Hit Locations."
