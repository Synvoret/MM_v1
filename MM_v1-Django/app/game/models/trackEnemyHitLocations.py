from django.db import models
from .game import Game


class TrackEnemyHitLocations(models.Model):
    """Presents a track for enemy hit locations values."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Track Enemy Hit locations"."""

        cls.hull = 1
        cls.cargo = 1
        cls.masts = 1
        cls.crew = 1
        cls.cannons = 1
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    hull = models.IntegerField(null=True, blank=True)
    cargo = models.IntegerField(null=True, blank=True)
    masts = models.IntegerField(null=True, blank=True)
    crew = models.IntegerField(null=True, blank=True)
    cannons = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Track Enemy Hit Locations."
