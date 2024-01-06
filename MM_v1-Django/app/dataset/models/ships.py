from django.db import models


class Ship(models.Model):
    """Ships plastic models for game."""

    COLOUR = [
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Treasure', 'Treasure')
    ]

    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50, null=True, blank=True, choices=COLOUR)
    image = models.ImageField(upload_to='ships/', blank=True, null=True)

    def __str__(self):
        return f"Ship - {self.name}"
