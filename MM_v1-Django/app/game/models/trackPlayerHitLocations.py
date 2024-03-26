from django.db import models
from dataset.utils.dataset.decorators.choices import HIT_LOCATIONS, PLAYER_COLOURS
from .game import Game
from game.models import PlayersShipsCards


class TrackPlayerHitLocations(models.Model):
    """Presents a track for player hit locations values."""

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.hull = 1
            field.cargo = 1
            field.masts = 1
            field.crew = 1
            field.cannons = 1
            field.save()

    def max_value_location(self, player: str, location: str) -> int:
        """Method returns maximum possible value for selected location, with all modifications, features, ship, etc."""
        location = location.lower()
        max_value = 0
        ship = getattr(PlayersShipsCards, player)

        if location == 'hull' or location == 'masts':
            max_value += ship.toughness
        elif location == 'cargo':
            max_value += ship.cargo
        elif location == 'crew':
            max_value += ship.crew
        elif location == 'cannons':
            max_value += ship.cannons

        return int(max_value)

    def value_location(self, location: str) -> int:
        """Method returns actual value for selected location."""
        location = location.lower()
        value = getattr(self, location)
        return int(value)

    def destroyed_location(self) -> bool:
        """Method returns False if any location isn't destroyed."""
        for location in HIT_LOCATIONS:
            if getattr(self, location) == 0:
                return True
        return False

    def damage_location(self, location: str):
        """Method update location when it receives damage."""
        location = location.lower()
        if getattr(self, location) > 0:
            setattr(self, location, getattr(self, location) - 1)
        self.save()

    def repair_location(self, player: str, location: str) -> bool:
        """Method update location when it repair."""
        location = location.lower()
        if self.value_location(location) >= self.max_value_location(player, location):
            return False
        else:
            setattr(self, location, getattr(self, location) + 1)
        self.save()
        return True

    def amount_damages(self, player: str) -> int:
        """Method return the total value of current damage to the ship."""
        amount = 0
        for location in HIT_LOCATIONS:
            amount += self.max_value_location(player, location) - getattr(self, location)
        return amount

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    player_colour = models.CharField(max_length=20, null=True, blank=True, choices=PLAYER_COLOURS)

    hull = models.IntegerField(default=1)
    cargo = models.IntegerField(default=1)
    masts = models.IntegerField(default=1)
    crew = models.IntegerField(default=1)
    cannons = models.IntegerField(default=1)

    def __str__(self):
        return f"Track Player {self.player_colour} Hit Locations."
