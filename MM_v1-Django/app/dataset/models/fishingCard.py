from django.db import models
from dataset.utils.dataset.decorators.choices import HITS
from .deck import Deck


class FishingCard(models.Model):
    """Description Fishing Card."""

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='fishingCards/', blank=True, null=True) # card front
    fishing_value = models.IntegerField(null=True, blank=True)
    fishing_hits = models.CharField(max_length=30, null=True, blank=True, choices=HITS)

    notes = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Fishing Card - {self.card}"
