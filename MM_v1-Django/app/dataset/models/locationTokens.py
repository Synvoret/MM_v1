from django.db import models


class LocationTokens(models.Model):
    """Model for location tokens."""

    class Meta:
        verbose_name = "Location Token"

    name = models.CharField(max_length=50)
    awers = models.ImageField(upload_to='locationTokens/', blank=True, null=True)

    def __str__(self):
        return f"Location Token - {self.name}"
