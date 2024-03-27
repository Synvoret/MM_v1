from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, SHIPS
from .deck import Deck


class ShipCard(models.Model):
    """Description Ship Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    ship = models.CharField(max_length=50, blank=True, null=True, choices=SHIPS)
    ship_type = models.IntegerField(blank=True, null=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='shipsCards/', blank=True, null=True) # card front
    toughness = models.IntegerField(blank=True, null=True)
    cargo = models.IntegerField(blank=True, null=True)
    crew = models.IntegerField(blank=True, null=True)
    cannons = models.IntegerField(blank=True, null=True)
    maneuverability = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    boats = models.IntegerField(blank=True, null=True)
    buy_cost = models.IntegerField(blank=True, null=True)
    sell_cost = models.IntegerField(blank=True, null=True)

    notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Ship - {self.ship}"
