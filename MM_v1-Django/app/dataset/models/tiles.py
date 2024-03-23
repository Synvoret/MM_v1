from django.db import models


class Tile(models.Model):
    """Separated elements from main board and player board as tiles."""

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tiles/', blank=True, null=True)

    def __str__(self):
        return f"Tile - {self.name}"
