from django.db import models


class Sign(models.Model):
    """Signs for game."""

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='signs/', blank=True, null=True)
    value = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Sign - {self.name}"
