from django.db import models


class Cube(models.Model):
    """Colorful cube udes in the game."""

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cubes/', blank=True, null=True)

    def __str__(self):
        return f"Cube - {self.name}"
