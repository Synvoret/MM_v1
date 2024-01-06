from django.db import models
from .game import Game
from dataset.models import CaptainCard


class PlayersCaptainsCards(models.Model):
    """Presents a Players Captains Cards for game."""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    player_blue = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_blue_captain_card')
    player_green = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_green_captain_card')
    player_red = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_red_captain_card')
    player_yellow = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_yellow_captain_card')

    def __str__(self):
        return f"Player Captain Card."
