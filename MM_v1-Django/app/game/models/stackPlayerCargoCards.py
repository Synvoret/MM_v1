import random
from django.db import models
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS
from .game import Game
from dataset.models import CargoCard


class StackPlayerCargoCards(models.Model):
    """Presents a Players Cargo Cards for game."""

    @classmethod
    def set_default_values(cls):
        fields = cls.objects.all()
        cargo_cards = CargoCard.objects.all()
        for field in fields:
            field.cargo_card_1 = None
            field.cargo_card_2 = None
            field.cargo_card_3 = None
            field.cargo_card_4 = None
            field.cargo_card_5 = None
            field.cargo_card_6 = None
            field.cargo_card_7 = None
            field.cargo_card_8 = None
            # if field.player_colour == 'red':
            #     field.cargo_card_1 = random.choice(cargo_cards)
            #     field.cargo_card_2 = random.choice(cargo_cards)
            #     field.cargo_card_3 = random.choice(cargo_cards)
            if field.player_colour == 'yellow':
                field.cargo_card_1 = random.choice(cargo_cards)
                field.cargo_card_2 = random.choice(cargo_cards)
                # field.cargo_card_3 = random.choice(cargo_cards)
                # field.cargo_card_4 = random.choice(cargo_cards)
                # field.cargo_card_5 = random.choice(cargo_cards)
                # field.cargo_card_6 = random.choice(cargo_cards)
                # field.cargo_card_7 = random.choice(cargo_cards)
                # field.cargo_card_8 = random.choice(cargo_cards)
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    player_colour = models.CharField(max_length=20, null=True, blank=True, choices=PLAYER_COLOURS)

    cargo_card_1 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_1')
    cargo_card_2 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_2')
    cargo_card_3 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_3')
    cargo_card_4 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_4')
    cargo_card_5 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_5')
    cargo_card_6 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_6')
    cargo_card_7 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_7')
    cargo_card_8 = models.ForeignKey(CargoCard, on_delete=models.CASCADE, null=True, blank=True, related_name='cargo_card_8')

    def __str__(self):
        return f"Player {self.player_colour} Cargo Cards."
