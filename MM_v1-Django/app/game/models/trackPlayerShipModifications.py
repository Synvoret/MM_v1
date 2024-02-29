from django.db import models
from .game import Game


class TrackPlayersShipModifications(models.Model):
    """Presents a track for player ship modifications."""

    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = list()
            field.player_green = list()
            field.player_red = list()
            field.player_yellow = list()
            field.player_yellow.append("Extended Cargo Hold")
            field.player_yellow.append("Advanced Rigs & Sails")
            field.player_yellow.append("Plank")
            field.player_yellow.append("Galley Refit")
            field.player_yellow.append("Carved Hull")
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.JSONField(default=list, null=True, blank=True)
    player_green = models.JSONField(default=list, null=True, blank=True)
    player_red = models.JSONField(default=list, null=True, blank=True)
    player_yellow = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"Track Player Special Weapons."
