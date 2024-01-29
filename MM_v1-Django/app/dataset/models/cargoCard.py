from django.db import models
from dataset.utils.dataset.decorators.choices import CARGO, DESTINATION_PORT, EXPANSION, HITS
# from dataset.utils.dataset.decorators.choices import choices
from .deck import Deck


# @choices
class CargoCard(models.Model):
    """Description Cargo Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, choices=CARGO)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='cargoCards/', blank=True, null=True) # card front

    cargo = models.CharField(max_length=150, null=True, blank=True, choices=CARGO)
    contraband_text = models.TextField(max_length=1000, null=True, blank=True)
    contraband_destination = models.CharField(max_length=150, null=True, blank=True, choices=DESTINATION_PORT)
    plunder_value = models.IntegerField(null=True, blank=True)
    hits = models.CharField(max_length=150, null=True, blank=True, choices=HITS)

    notes = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Cargo Card - {self.card}"
