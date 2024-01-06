from django.db import models
from .game import Game


class TrackPlayerGolds(models.Model):
    """Presents a track for player golds."""

    COLOURS = [
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
    ]

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)
    player_colour = models.CharField(max_length=20, null=True, blank=True, choices=COLOURS)

    amount_gold = models.IntegerField(default=10)

    def __str__(self):
        return f"Track Player Golds."