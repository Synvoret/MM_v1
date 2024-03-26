from django.db import models
from .game import Game


class TrackPlayersShipModifications(models.Model):
    """Presents a track for player ship modifications."""

    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        # cls.objects.filter(...).update(player_blue=[], player_green=[], player_red=[], player_yellow=[])

        for field in fields:
            field.player_blue = list()
            field.player_green = list()
            field.player_red = list()
            field.player_yellow = list()
            field.save()

    def add_modification(self, colour: str, modification: str):
        """Method add modification for Player Ship and return True, if possible, otherwise return False."""
        player_list = list(getattr(self, f"player_{colour}"))
        if modification in player_list:
            return False
        else:
            player_list.append(modification)
            setattr(self, f"player_{colour}", player_list)
        self.save()
        return True

    def remove_modification(self, colour: str, modification: str):
        player_list = list(getattr(self, f"player_{colour}"))
        if modification in player_list:
            player_list.remove(modification)
            setattr(self, f"player_{colour}", player_list)
        self.save()

    def amount_modifications(self, colour: str) -> int:
        amount = len(getattr(self, f"player_{colour}"))
        return amount

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.JSONField(default=list, null=True, blank=True)
    player_green = models.JSONField(default=list, null=True, blank=True)
    player_red = models.JSONField(default=list, null=True, blank=True)
    player_yellow = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"Track Player Special Weapons."
