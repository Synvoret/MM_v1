from django.db import models


class Cube(models.Model):
    """Colorful cube uses in the game."""

    @classmethod
    def player_cube(cls, colour: str):
        image = cls.objects.get(name=f"{colour.capitalize()} Cube")
        return image.image.url

    @classmethod
    def player_cube_max(cls, colour: str):
        image = cls.objects.get(name=f"{colour.capitalize()} Cube Max")
        return image.image.url

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cubes/', blank=True, null=True)

    def __str__(self):
        return f"Cube - {self.name}"
