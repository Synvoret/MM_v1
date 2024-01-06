from django.db import models
from .game import Game
from dataset.models import ShipCard


class PlayersShipsCards(models.Model):
    """Presents a Players Ships Cards for game."""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    player_blue = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_blue_ship_card')
    player_green = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_green_ship_card')
    player_red = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_red_ship_card')
    player_yellow = models.ForeignKey(ShipCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_yellow_ship_card')

    def __str__(self):
        return f"Player Ship Card."
