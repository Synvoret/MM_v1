from django.db import models
from .deck import Deck


class GloryCard(models.Model):
    """Description Glory Card."""

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    awers = models.ImageField(upload_to='gloryCards/', blank=True, null=True) # card front
    rewers = models.ImageField(blank=True, null=True) # card back

    def __str__(self):
        return f"Glory - {self.card}"
