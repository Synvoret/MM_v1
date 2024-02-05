from django.db import models
from dataset.utils.dataset.decorators.choices import NATIONALITY
from .backs import Back


class MerchantTokens(models.Model):
    """Model for merchants tokens."""

    class Meta:
        verbose_name = "Merchant Token"

    name = models.CharField(max_length=50)
    awers = models.ImageField(upload_to='merchantTokens/', blank=True, null=True)
    rewers = models.ForeignKey(Back, on_delete=models.SET_NULL, blank=True, null=True)
    nationality = models.CharField(max_length=20, null=True, blank=True, choices=NATIONALITY)

    def __str__(self):
        return f"Merchant token - {self.name}"
