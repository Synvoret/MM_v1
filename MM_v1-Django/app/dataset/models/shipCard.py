from django.db import models
from .deck import Deck


class ShipCard(models.Model):    
    """Description Ship Card."""

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    ship = models.CharField(max_length=50, blank=True, null=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='shipsCards/', blank=True, null=True) # card front
    toughness = models.IntegerField(blank=True, null=True)
    cargo = models.IntegerField(blank=True, null=True)
    crew = models.IntegerField(blank=True, null=True)
    cannons = models.IntegerField(blank=True, null=True)
    maneuverability = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    boats = models.IntegerField(blank=True, null=True)

    notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Ship - {self.ship}"
