from django.db import models
from .game import Game
from dataset.models import ShipCard


class PlayersShipsCards(models.Model):
    """Presents a Players Ships Cards for game."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Player Ship"."""
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = None
            field.player_green = None
            field.player_red = None
            field.player_yellow = None
            field.save()

    def change_ship_unit(self, colour: str, ship: str):
        new_unit = ShipCard.objects.get(ship=ship, ship_type=3)
        setattr(self, f"player_{colour}", new_unit)
        self.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_blue_ship_card')
    player_green = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_green_ship_card')
    player_red = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_red_ship_card')
    player_yellow = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_yellow_ship_card')

    def __str__(self):
        return f"Player Ship Card."
