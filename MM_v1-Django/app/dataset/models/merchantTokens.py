from django.db import models
from .backs import Back


class MerchantTokens(models.Model):
    """Model for merchants tokens."""

    class Meta:
        verbose_name = "Merchant Token"

    NATIONALITY = [
        ('Dutch', 'Dutch'),
        ('French', 'French'),
        ('English', 'English'),
        ('Spanish', 'Spanich'),
    ]

    name = models.CharField(max_length=50)
    awers = models.ImageField(upload_to='merchantTokens/', blank=True, null=True)
    rewers = models.ForeignKey(Back, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Merchant token - {self.name}"
