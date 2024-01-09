from django.db import models
from .game import Game


class TrackPlayerGolds(models.Model):
    """Presents a track for player golds."""

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    player_blue = models.IntegerField(default=0)
    player_green = models.IntegerField(default=0)
    player_red = models.IntegerField(default=0)
    player_yellow = models.IntegerField(default=0)

    def __str__(self):
        return f"Track Player Golds."
