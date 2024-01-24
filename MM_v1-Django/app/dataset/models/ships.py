from django.db import models
from dataset.utils.dataset.decorators.choices import COLOUR, SHIPS


class Ship(models.Model):
    """Ships plastic models for game."""

    name = models.CharField(max_length=50, choices=SHIPS)
    colour = models.CharField(max_length=50, null=True, blank=True, choices=COLOUR)
    image = models.ImageField(upload_to='ships/', blank=True, null=True)

    def __str__(self):
        return f"Ship - {self.name}"
