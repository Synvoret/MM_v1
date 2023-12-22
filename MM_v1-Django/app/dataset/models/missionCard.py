from django.db import models
from .deck import Deck

class MissionCard(models.Model):
    """Description Mission Card."""

    PORT = [
        ('Basse-Terre', 'Basse-Terre'),
        ('Bridgetown', 'Bridgetown'),
        ('Caracas', 'Caracas'),
        ('Cartagena', 'Cartagena'),
        ('Curacao', 'Curacao'),
        ('Havana', 'Havana'),
        ('Nassau', 'Nassau'),
        ('Old Providence', 'Old Providence'),
        ('Petite Goave', 'Petite Goave'),
        ('Port Royal', 'Port Royal'),
        ('San Juan', 'San Juan'),
        ('Santo Domingo', 'Santo Domingo'),
        ('St. John', 'St. John'),
        ('St. Maarten', 'St. Maarten'),
        ('Tortuga', 'Tortuga'),
        ('Trinidad', 'Trinidad'),
    ]

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=50, unique=True)
    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    awers = models.ImageField(upload_to='missionsCards/', blank=True, null=True) # card front
    rewers = models.ImageField(blank=True, null=True) # card back
    earn = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)
    port = models.CharField(max_length=100, choices=PORT)

    def __str__(self):
        return f"Mission - {self.card}"
