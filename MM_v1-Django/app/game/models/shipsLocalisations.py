from django.db import models
from dataset.utils.dataset.decorators.choices import SEAZONES
from .game import Game


class ShipsLocalisations(models.Model):
    """Presents a localisations ships on the board."""

    # @classmethod
    # def set_default_values(cls):
    #     # Pobierz listę pól modelu
    #     fields = cls._meta.get_fields()

    #     # Iteruj przez pola i ustaw wartości domyślne
    #     for field in fields:
    #         if isinstance(field, models.Field):
    #             setattr(cls, field.attname, field.default)

    #     # Zapisz zmieniony obiekt modelu
    #     cls().save()


    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        for field in fields:
            field.blue_ship = None
            field.blue_in_port = False
            field.green_ship = None
            field.green_in_port = False
            field.red_ship = None
            field.red_in_port = False
            field.yellow_ship = None
            field.yellow_in_port = False
            field.merchants = None
            field.dutch_ship = None
            field.english_ship = None
            field.french_ship = None
            field.spanish_ship = None
            field.small_pirate_ship = None
            field.large_pirate_ship = None
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    blue_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    blue_in_port = models.BooleanField(default=False)
    green_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    green_in_port = models.BooleanField(default=False)
    red_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    red_in_port = models.BooleanField(default=False)
    yellow_ship = models.CharField(max_length=100, default=None, null=True, blank=True, choices=SEAZONES)
    yellow_in_port = models.BooleanField(default=False)

    merchants_ship = models.JSONField(default=None, null=True, blank=True)
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