from django.db import models
from .game import Game
from dataset.models import CaptainCard


class PlayersCaptainsCards(models.Model):
    """Presents a Players Captains Cards for game."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "Player Captain"."""
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = None
            field.player_green = None
            field.player_red = None
            field.player_yellow = None
            field.save()

    def change_captain(self, colour: str, captain: str):
        new_captain = CaptainCard.objects.get(captain=captain)
        setattr(self, f"player_{colour}", new_captain)
        self.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_blue_captain_card', default=None)
    player_green = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_green_captain_card', default=None)
    player_red = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_red_captain_card', default=None)
    player_yellow = models.ForeignKey(CaptainCard, on_delete=models.CASCADE, null=True, blank=True, related_name='player_yellow_captain_card', default=None)

    def __str__(self):
        return f"Player Captain Card."
