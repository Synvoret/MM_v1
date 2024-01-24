from django.db import models
from dataset.utils.dataset.decorators.choices import LOYALITY
from .game import Game


class TrackLoyality(models.Model):
    """Presents a track for crew loyality."""

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    player_blue = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_green = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_red = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_yellow = models.CharField(max_length=20, default='Content', choices=LOYALITY)

    def __str__(self):
        return f"Track Crew Loyality."
