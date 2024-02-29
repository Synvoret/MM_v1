from django.db import models
from .game import Game


class TrackPlayerBounties(models.Model):
    """Presents a track for player bounties."""

    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = list()
            field.player_green = list()
            field.player_red = list()
            field.player_yellow = list()
            # field.player_yellow.append("English")
            # field.player_yellow.append("Dutch")
            # field.player_yellow.append("English")
            # field.player_yellow.append("French")
            # field.player_red.append("French")
            # field.player_red.append("French")
            # field.player_yellow.append("Spanish")
            # field.player_yellow.append("Small Pirate")
            # field.player_yellow.append("Small Pirate")
            # field.player_red.append("Small Pirate")
            # field.player_yellow.append("Small Pirate")
            # field.player_yellow.append("Small Pirate")
            # field.player_yellow.append("Large Pirate")
            # field.player_yellow.append("Large Pirate")
            # field.player_yellow.append("Large Pirate")
            # field.player_yellow.append("Large Pirate")
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.JSONField(default=list, null=True, blank=True)
    player_green = models.JSONField(default=list, null=True, blank=True)
    player_red = models.JSONField(default=list, null=True, blank=True)
    player_yellow = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"Track Player Bounties."
