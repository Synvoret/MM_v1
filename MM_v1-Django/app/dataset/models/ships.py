from django.db import models


class Ship(models.Model):
    """Ships plastic models for game."""

    COLOUR = [
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Dutch', 'Dutch'),
        ('English', 'English'),
        ('French', 'French'),
        ('Green', 'Green'),
        ('Large Pirate', 'Large Pirate'),
        ('Pirate', 'Pirate'),
        ('Red', 'Red'),
        ('Small Pirate', 'Small Pirate'),
        ('Spanish', 'Spanish'),
        ('Yellow', 'Yellow'),
        ('Treasure', 'Treasure'),
    ]

    SHIPS = [
        ('Brig', 'Brig'),
        ('Flute', 'Flute'),
        ('Frigate', 'Frigate'),
        ('Galleon', 'Galleon'),
        ('Man-o-War', 'Man-o-War'),
        ('Sloop', 'Sloop'),
    ]

    name = models.CharField(max_length=50, choices=SHIPS)
    colour = models.CharField(max_length=50, null=True, blank=True, choices=COLOUR)
    image = models.ImageField(upload_to='ships/', blank=True, null=True)

    def __str__(self):
        return f"Ship - {self.name}"
