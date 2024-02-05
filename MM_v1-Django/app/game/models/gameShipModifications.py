from django.db import models
from .game import Game


class GameShipModifications(models.Model):
    """Ship Modification Tokens for Game."""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    basse_terre = models.CharField(max_length=20, null=True, blank=True)
    bridgetown = models.CharField(max_length=20, null=True, blank=True)
    caracas = models.CharField(max_length=20, null=True, blank=True)
    cartagena = models.CharField(max_length=20, null=True, blank=True)
    curacao = models.CharField(max_length=20, null=True, blank=True)
    gulf_city = models.CharField(max_length=20, null=True, blank=True)
    nassau = models.CharField(max_length=20, null=True, blank=True)
    havana = models.CharField(max_length=20, null=True, blank=True)
    old_providence = models.CharField(max_length=20, null=True, blank=True)
    petite_goave = models.CharField(max_length=20, null=True, blank=True)
    port_royal = models.CharField(max_length=20, null=True, blank=True)
    san_juan = models.CharField(max_length=20, null=True, blank=True)
    santo_domingo = models.CharField(max_length=20, null=True, blank=True)
    st_john = models.CharField(max_length=20, null=True, blank=True)
    st_maarten = models.CharField(max_length=20, null=True, blank=True)
    trinidad = models.CharField(max_length=20, null=True, blank=True)
    tortuga = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.game_number} Ship Modification."
