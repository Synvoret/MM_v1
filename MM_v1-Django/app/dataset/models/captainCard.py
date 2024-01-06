from django.db import models
from .deck import Deck


class CaptainCard(models.Model):
    """Description Captain Card."""

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

    NATIONALITY = [
        ('DU', 'Dutch'),
        ('FR', 'French'),
        ('EN', 'English'),
        ('SP', 'Spanich'),
    ]

    EXPANSION = [
        ('Seas of Glory', 'Seas of Glory'),
        ('Colors of War', 'Colors of War'),
    ]

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
