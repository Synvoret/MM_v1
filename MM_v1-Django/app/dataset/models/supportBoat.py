from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, SUPPORTBOATS
from .deck import Deck


class SupportBoatCard(models.Model):    
    """Description Support Boat Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    boat = models.CharField(max_length=50, blank=True, null=True, choices=SUPPORTBOATS)
    boat_type = models.IntegerField(blank=True, null=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='supportBoatsCards/', blank=True, null=True) # card front
    toughness = models.IntegerField(blank=True, null=True)
    cargo = models.IntegerField(blank=True, null=True)
    crew = models.IntegerField(blank=True, null=True)
    cannons = models.IntegerField(blank=True, null=True)
    maneuverability = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    seamanship = models.IntegerField(blank=True, null=True)
    leadership = models.IntegerField(blank=True, null=True)
    buy_cost = models.IntegerField(blank=True, null=True)
    sell_cost = models.IntegerField(blank=True, null=True)

    notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Boat - {self.boat}"
