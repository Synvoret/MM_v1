from django.db import models
from .deck import Deck


class ShipCard(models.Model):    
    """Description Ship Card."""

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    awers = models.ImageField(upload_to='shipsCards/', blank=True, null=True) # card front
    rewers = models.ImageField(blank=True, null=True) # card back
    toughness = models.IntegerField()
    cargo = models.IntegerField()
    crew = models.IntegerField()
    cannons = models.IntegerField()
    maneuverability = models.IntegerField()

    def __str__(self):
        return f"Ship - {self.card}"
