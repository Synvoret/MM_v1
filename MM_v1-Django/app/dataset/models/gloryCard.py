from django.db import models
from dataset.utils.dataset.decorators.choices import EXPANSION
from .deck import Deck


class GloryCard(models.Model):
    """Description Glory Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='gloryCards/', blank=True, null=True) # card front
    
    notes = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Glory - {self.card}"
