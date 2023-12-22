from django.db import models
from .deck import Deck


class RumorCard(models.Model):
    """Description Rumor Card."""

    SKILL = [
        ('Scouting', 'Scouting'),
        ('Influence', 'Influence'),
    ]

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    awers = models.ImageField(upload_to='rumorsCards/', blank=True, null=True) # card front
    rewers = models.ImageField(blank=True, null=True) # card back
    require = models.CharField(max_length=200)
    skill_test = models.CharField(max_length=10, choices=SKILL)

    notes = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"Rumor - {self.card}"
