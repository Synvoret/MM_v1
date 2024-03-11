from django.db import models
from .game import Game


class TrackGloryPoint(models.Model):
    """Presents a track for glory points players values."""

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = 0
            field.player_green = 0
            field.player_red = 0
            field.player_yellow = 0
            field.save()

    def increase_glory_point(self, player: str):
        """Increase glory point by 1 point (max. 20)."""
        if getattr(self, player) == 20: 
            return
        else:
            setattr(self, player, getattr(self, player) + 1)
            self.save()

    def decrease_glory_point(self, player: str):
        """Decrease glory point by 1 point (min. 0)."""
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
        return f"Track Glory Points."
