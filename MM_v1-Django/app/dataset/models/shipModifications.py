from django.db import models
from .backs import Back


class ShipModifications(models.Model):
    """Model for ship modifications."""

    class Meta:
        verbose_name = "Ship Modification Token"

    name = models.CharField(max_length=50)
    awers = models.ImageField(upload_to='shipModifications/', blank=True, null=True)
    rewers = models.ForeignKey(Back, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Ship modification - {self.name}"
