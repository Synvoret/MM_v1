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

    def increase_golds(self, player: str, amount: int):
        """Increase Golds by amount."""
        setattr(self, player, getattr(self, player) + amount)
        self.save()

    def decrease_golds(self, player: str, amount: int):
        """Decrease Golds by amount, return True if possible"""
        if getattr(self, player) < amount:
            return False
        else:
            setattr(self, player, getattr(self, player) - amount)
        self.save()
        return True

    def change_golds(self, player: str, amount: int):
        """Change golds by amount."""
        setattr(self, player, amount)
        self.save()

    def golds_amount(self, player: str) -> int:
        golds_amount = getattr(self, f"player_{player}")
        return golds_amount

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.IntegerField(default=10)
    player_green = models.IntegerField(default=10)
    player_red = models.IntegerField(default=10)
    player_yellow = models.IntegerField(default=10)

    def __str__(self):
        return f"Track Player Golds."
