from django.db import models
from .board import Board
from dataset.models import MissionCard


class TrackMissions(models.Model):
    """Present a missions one on board"""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    card_one = models.ForeignKey(MissionCard, on_delete=models.CASCADE, related_name="mission_one")
    card_two = models.ForeignKey(MissionCard, on_delete=models.CASCADE, related_name="mission_two")

    def __str__(self):
        return f"Track mission one on board - {self.board}"


class TrackEnemyHitLocation(models.Model):
    """Presents a track with enemy hit location on board."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    hull = models.IntegerField(default=0)
    cargo = models.IntegerField(default=0)
    masts = models.IntegerField(default=0)
    crew = models.IntegerField(default=0)
    cannons = models.IntegerField(default=0)

    def __str__(self):
        return f"Track enemy hit location for board - {self.board}"


class TrackMerchantToken(models.Model):
    """Presents a track for raided merchant tokens."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    thirth = models.BooleanField(default=False)
    fourth = models.BooleanField(default=False)
    fifth = models.BooleanField(default=False)
    sixth = models.BooleanField(default=False)
    seventh = models.BooleanField(default=False)
    eighth = models.BooleanField(default=False)

    def __str__(self):
        return f"Track merchant tokens for board - {self.board}"


class TrackGloryPoints(models.Model):
    """Presents a track glory points and each player position on it."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    blue_player = models.IntegerField(default=0)
    green_player = models.IntegerField(default=0)
    red_player = models.IntegerField(default=0)
    yellow_player = models.IntegerField(default=0)

    def __str__(self):
        return f"Track glory points for board - {self.board}"


class TrackAtWar(models.Model):
    """Presents a war section on board."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    section_left = models.CharField(max_length=20)
    section_right = models.CharField(max_length=20)

    def __str__(self):
        return f"At war on board - {self.board}"
