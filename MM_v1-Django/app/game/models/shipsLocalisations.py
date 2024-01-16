from django.db import models
from .game import Game


class ShipsLocalisations(models.Model):
    """Presents a localisations ships on the board."""

    SEAZONES = [
        ('Basse-Terre', 'Basse-Terre'),
        ('Bridgetown', 'Bridgetown'),
        ('Caracas', 'Caracas'),
        ('Cartagena', 'Cartagena'),
        ('Curacao', 'Curacao'),
        ('Gulf City', 'Gulf City'),
        ('Havana', 'Havana'),
        ('Nassau', 'Nassau'),
        ('Old Providence', 'Old Providence'),
        ('Petite Goave', 'Petite Goave'),
        ('Port Royal', 'Port Royal'),
        ('San Juan', 'San Juan'),
        ('Santo Domingo', 'Santo Domingo'),
        ('St John', 'St John'),
        ('St Maarten', 'St Maarten'),
        ('The Carribean Sea', 'The Carribean Sea'),
        ('Tortuga', 'Tortuga'),
        ('Trinidad', 'Trinidad'),
    ]

    def set_default_values(self):
        self.blue_ship =None
        self.green_ship = None
        self.red_ship = None
        self.yellow_ship = None
        self.dutch_ship = None
        self.english_ship = None
        self.french_ship = None
        self.spanish_ship = None
        self.small_pirate_ship = None
        self.large_pirate_ship = None


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