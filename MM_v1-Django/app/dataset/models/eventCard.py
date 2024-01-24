from django.db import models
from dataset.utils.dataset.decorators.choices import DIRECTION, EXPANSION, NATIONALITY, SEAZONES, SHIPS
from .deck import Deck


class EventCard(models.Model):
    """Event Card."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.CharField(max_length=100, unique=True, null=True, blank=True)

    expansion = models.CharField(max_length=150, null=True, blank=True, choices=EXPANSION)
    awers = models.ImageField(upload_to='eventsCards/', blank=True, null=True) # card front

    moving = models.BooleanField(default=False)
    dutch_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    english_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    french_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    spanish_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    large_pirate_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)
    small_pirate_direction = models.CharField(max_length=2, null=True, blank=True, choices=DIRECTION)

    # if event its NPC Player
    nationality = models.CharField(max_length=50, null=True, blank=True, choices=NATIONALITY)
    sea_zone_start = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    ship = models.CharField(max_length=50, null=True, blank=True, choices=SHIPS)
    npc_name = models.CharField(max_length=150, null=True, blank=True)
    seamanship = models.IntegerField(null=True, blank=True)
    scouting = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)
    reward = models.IntegerField(null=True, blank=True)

    notes = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Event - {self.card}"
