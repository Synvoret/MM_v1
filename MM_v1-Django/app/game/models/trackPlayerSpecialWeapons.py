from django.db import models
from .game import Game


class TrackPlayerSpecialWeapons(models.Model):
    """Presents a track for player special weapons."""

    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = list()
            field.player_green = list()
            field.player_red = list()
            field.player_yellow = list()
            field.player_yellow.append("Chain Shot")
            field.player_yellow.append("Grapeshot")
            field.player_yellow.append("Grappling Hooks")
            field.player_yellow.append("Double Shot")
            # field.player_yellow.append("Caltrops")
            field.player_yellow.append("Heated Shot")
            field.player_yellow.append("Grenade")
            field.player_yellow.append("Premium Rum")
            field.player_yellow.append("Explosive Shell")
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.JSONField(default=list, null=True, blank=True)
    player_green = models.JSONField(default=list, null=True, blank=True)
    player_red = models.JSONField(default=list, null=True, blank=True)
    player_yellow = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"Track Player Special Weapons."
