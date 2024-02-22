from django.db import models
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS
from .game import Game


class TrackPlayerHitLocations(models.Model):
    """Presents a track for player hit locations values."""

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.hull = 1
            field.cargo = 1
            field.masts = 1
            field.crew = 1
            field.cannons = 1
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    player_colour = models.CharField(max_length=20, null=True, blank=True, choices=PLAYER_COLOURS)

    hull = models.IntegerField(default=1)
    cargo = models.IntegerField(default=1)
    masts = models.IntegerField(default=1)
    crew = models.IntegerField(default=1)
    cannons = models.IntegerField(default=1)

    def __str__(self):
        return f"Track Player {self.player_colour} Hit Locations."
