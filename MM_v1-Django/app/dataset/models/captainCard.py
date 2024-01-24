from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, NATIONALITY, PORT
from .deck import Deck


class CaptainCard(models.Model):
    """Description Captain Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    captain = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='captainCards/', blank=True, null=True) # card front
    home_port = models.CharField(max_length=30, choices=PORT, blank=True, null=True)
    nationality = models.CharField(max_length=30, choices=NATIONALITY)
    seamanship = models.IntegerField(blank=True, null=True)
    scouting = models.IntegerField(blank=True, null=True)
    leadership = models.IntegerField(blank=True, null=True)
    influence = models.IntegerField(blank=True, null=True)
    notes = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"Captain - {self.captain}"
