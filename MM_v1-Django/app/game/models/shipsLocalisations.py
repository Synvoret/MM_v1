from django.db import models
from dataset.utils.dataset.decorators.choices import SEAZONES
from .game import Game


class ShipsLocalisations(models.Model):
    """Presents a localisations ships on the board."""

    @classmethod
    def set_default_values(cls):

        cls.blue_ship =None
        cls.green_ship = None
        cls.red_ship = None
        cls.yellow_ship = None
        cls.dutch_ship = None
        cls.english_ship = None
        cls.french_ship = None
        cls.spanish_ship = None
        cls.small_pirate_ship = None
        cls.large_pirate_ship = None

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)

    blue_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    green_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    red_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    yellow_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)

    dutch_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    english_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    french_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    spanish_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)

    small_pirate_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    large_pirate_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)

    def __str__(self):
        return f"Ships Localisations."

    # def save(self, *args, **kwargs):
    #     # If card_event is not already assigned, assign a random event card
    #     if not self.card_event:
    #         self.random_event_card()

    #     super().save(*args, **kwargs)