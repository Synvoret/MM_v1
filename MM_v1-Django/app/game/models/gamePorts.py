from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, NATIONALITY, SEAZONES
from game.models import Game
from dataset.models import PortCard


class GamePorts(models.Model):
    """Presents a current situation on Port."""

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)


    def __str__(self):
        return f"Port {self.sea_zone}."
