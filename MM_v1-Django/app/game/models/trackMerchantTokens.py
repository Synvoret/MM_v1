from django.db import models
from .game import Game


class TrackMerchantTokens(models.Model):
    """Presents a track Merchant Tokens on board."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values.."""

        fields = cls.objects.all()
        for field in fields:
            field.first = None
            field.second = None
            field.thrith = None
            field.fourth = None
            field.fivth = None
            field.sixth = None
            field.seventh = None
            field.eighth = None
            field.save()


    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    first = models.CharField(max_length=30, null=True, blank=True)
    second = models.CharField(max_length=30, null=True, blank=True)
    thrith = models.CharField(max_length=30, null=True, blank=True)
    fourth = models.CharField(max_length=30, null=True, blank=True)
    fivth = models.CharField(max_length=30, null=True, blank=True)
    sixth = models.CharField(max_length=30, null=True, blank=True)
    seventh = models.CharField(max_length=30, null=True, blank=True)
    eighth = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"Track Merchant Tokens for {self.game_number}."
