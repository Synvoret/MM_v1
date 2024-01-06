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

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='eventsCards/', blank=True, null=True) # card front
    dutch_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    english_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    french_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    spanish_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    pirateFrigate_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    pirateSloop_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Event - {self.card}"
