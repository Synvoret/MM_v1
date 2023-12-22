from django.db import models


class Deck(models.Model):
    """Deck model for all card decks in game."""

    deck = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Deck - {self.deck}"
