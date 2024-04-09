from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, NATIONALITY, SEAZONES
from dataset.models import PortCard
from game.models import Game


class GamePorts(models.Model):
    """Presents a current situation on Port."""

    @classmethod
    def set_default_values(cls):
        pass

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    port_data = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f"Port data for  {self.game_number}."
