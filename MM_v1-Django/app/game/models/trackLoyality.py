from django.db import models
from dataset.utils.dataset.decorators.choices import LOYALITY, LOYALITIES
from .game import Game


class TrackLoyality(models.Model):
    """Presents a track for crew loyality."""

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = 'Content'
            field.player_green = 'Content'
            field.player_red = 'Content'
            field.player_yellow = 'Content'
            field.save()

    def increase_loyality(self, player: str):
        """Increase loyality."""
        if getattr(self, player) == 'Fierce Loyality': # cant increase more
            return
        else:
            index = LOYALITIES.index(getattr(self, player))
            if index == 0:
                return
            else:
                setattr(self, player, LOYALITIES[index - 1])
                self.save()

    def decrease_loyality(self, player: str):
        """Decrease loyality."""
        if getattr(self, player) == 'Angry': # mutiny!
            print('LOYALITy SPADŁO NA MUTINY, TEST NA BUNT!!!!!!!!!!!!! (track loyality game.models)')
            return
        else:
            index = LOYALITIES.index(getattr(self, player))
            setattr(self, player, LOYALITIES[index + 1])
            self.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_green = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_red = models.CharField(max_length=20, default='Content', choices=LOYALITY)
    player_yellow = models.CharField(max_length=20, default='Content', choices=LOYALITY)

    def __str__(self):
        return f"Track Crew Loyality."


# for x in LOYALITY:
#     print(x[0])