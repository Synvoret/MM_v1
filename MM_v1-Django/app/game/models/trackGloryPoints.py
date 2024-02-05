from django.db import models
from .game import Game


class TrackGloryPoint(models.Model):
    """Presents a track for glory points players values."""

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.IntegerField(default=0)
    player_green = models.IntegerField(default=0)
    player_red = models.IntegerField(default=0)
    player_yellow = models.IntegerField(default=0)

    def __str__(self):
        return f"Track Glory Points."
