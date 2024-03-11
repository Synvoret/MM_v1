from django.db import models
from .game import Game


class TrackFavors(models.Model):
    """Presents a track for Favors."""

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = 0
            field.player_green = 0
            field.player_red = 0
            field.player_yellow = 0
            field.save()

    def increase_favour_point(self, player: str):
        """Increase favour point by 1 point (max. 5)."""
        if getattr(self, player) == 5:
            return
        else:
            setattr(self, player, getattr(self, player) + 1)
            self.save()

    def decrease_favour_point(self, player: str):
        """Decrease favour point by 1 point (min. 0)."""
        if getattr(self, player) == 0:
            return
        else:
            setattr(self, player, getattr(self, player) - 1)
            self.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.IntegerField(default=0)
    player_green = models.IntegerField(default=0)
    player_red = models.IntegerField(default=0)
    player_yellow = models.IntegerField(default=0)

    def __str__(self):
        return f"Track Favors."
