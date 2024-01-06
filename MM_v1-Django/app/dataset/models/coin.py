from django.db import models


class Coin(models.Model):
    """Coin model."""

    VALUE = [
        (1, 1),
        (3, 3),
        (5, 5),
        (10, 10),
    ]

    coin = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='coins/', blank=True, null=True)
    value = models.IntegerField(choices=VALUE, null=True, blank=True)

    def __str__(self):
        return f"Coin - {self.coin}"
