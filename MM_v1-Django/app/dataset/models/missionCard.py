from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, PORT
from .deck import Deck

class MissionCard(models.Model):
    """Description Mission Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=100, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='missionsCards/', blank=True, null=True) # card front
    earn = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)
    port = models.CharField(max_length=100, choices=PORT)
    notes = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"Mission - {self.card}"
