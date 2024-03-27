from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION, NATIONALITY, SEAZONES
from .deck import Deck


class PortCard(models.Model):
    """Presents a Port Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True, blank=True, )
    sea_zone = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    image = models.ImageField(upload_to='portsCards/', blank=True, null=True)
    expansion = models.CharField(max_length=50, null=True, blank=True, choices=EXPANSION)
    nationality = models.CharField(max_length=50, null=True, blank=True, choices=NATIONALITY)
    fortitude = models.IntegerField(null=True, blank=True)
    stockpile = models.IntegerField(null=True, blank=True)
    soldiers = models.IntegerField(null=True, blank=True)
    cannons = models.IntegerField(null=True, blank=True)
    defensibility = models.IntegerField(null=True, blank=True)
    boats = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Port {self.sea_zone} Card."
