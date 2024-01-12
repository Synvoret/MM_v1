from django.db import models
from .deck import Deck


class EventCard(models.Model):
    """Event Card."""

    DIRECTION = [
            ('N', 'North'),
            ('NE', 'Northeast'),
            ('E', 'East'),
            ('SE', 'Southeast'),
            ('S', 'South'),
            ('SW', 'Southwest'),
            ('W', 'West'),
            ('NW', 'Northwest'),
        ]

    EXPANSION = [
            ('Seas of Glory', 'Seas of Glory'),
            ('Colors of War', 'Colors of War'),
        ]

    NATIONALITY = [
            ('Dutch', 'Dutch'),
            ('English', 'English'),
            ('French', 'French'),
            ('Spanish', 'Spanish'),
            ('Small Pirate', 'Small Pirate'),
            ('Large Pirate', 'Large Pirate'),
        ]

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

    SHIPS = [
            ('Brig', 'Brig'),
            ('Flute', 'Flute'),
            ('Frigate', 'Frigate'),
            ('Galleon', 'Galleon'),
            ('Man-o-War', 'Man-o-War'),
            ('Sloop', 'Sloop'),
        ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=100, unique=True, null=True, blank=True)

    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='eventsCards/', blank=True, null=True) # card front

    moving = models.BooleanField(default=False)
    dutch_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    english_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    french_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    spanish_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    large_pirate_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    small_pirate_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)

    # if event its NPC Player
    nationality = models.CharField(max_length=50, null=True, blank=True, choices=NATIONALITY)
    sea_zone_start = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    ship = models.CharField(max_length=50, null=True, blank=True, choices=SHIPS)
    npc_name = models.CharField(max_length=150, null=True, blank=True)
    seamanship = models.IntegerField(null=True, blank=True)
    scouting = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)
    reward = models.IntegerField(null=True, blank=True)

    notes = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Event - {self.card}"
