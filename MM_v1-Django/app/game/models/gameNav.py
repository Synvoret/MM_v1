from django.db import models
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS
from .game import Game


class gameNav(models.Model):
    """Presents a Players Captains Cards for game."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Player Captain"."""
        pass

        # cls.player_blue = None
        # cls.player_green = None
        # cls.player_red = None
        # cls.player_yellow = None

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    player_colour = models.CharField(max_length=30, null=True, blank=True, choices=PLAYER_COLOURS)

    



    def __str__(self):
        return f"Player Captain Card."
