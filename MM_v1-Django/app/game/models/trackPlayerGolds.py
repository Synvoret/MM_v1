from django.db import models
from .game import Game


class TrackPlayerGolds(models.Model):
    """Presents a track for player golds."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all players golds."""

        fields = cls.objects.all()
        for field in fields:
            field.player_blue = 10
            field.player_green = 10
            field.player_red = 10
            field.player_yellow = 10
            field.save()


    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.IntegerField(default=10)
    player_green = models.IntegerField(default=10)
    player_red = models.IntegerField(default=10)
    player_yellow = models.IntegerField(default=10)

    def __str__(self):
        return f"Track Player Golds."
