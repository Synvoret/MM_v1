from django.db import models


class DemandTokens(models.Model):
    """Model for demand tokens."""

    class Meta:
        verbose_name = "Demand Token"

    cargo = models.CharField(max_length=20)
    awers = models.ImageField(upload_to='demandTokens/', blank=True, null=True)

    def __str__(self):
        return f"Demand Token - {self.cargo}"
