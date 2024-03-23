import random
from django.db import models
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS
from dataset.models import CargoCard
from .game import Game

class StackPlayerCargoCards(models.Model):
    """Presents a Players Cargo Cards in Ship's Hold for game."""

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
            field.save()

    def add_cargo_card(self, cargo_card_id: int):
        """Method adds a cargo card to nearest free space in ship's hold."""
        cargo_card = CargoCard.objects.get(id=cargo_card_id)
        for i in range(1, 9):
            if getattr(self, f"cargo_card_{i}") is None:
                setattr(self, f"cargo_card_{i}", cargo_card)
                self.save()
                break

    def remove_cargo_card(self):
        """Method removes selected cargo card from ship's hold."""
        pass

    def random_discard_cargo_card(self):
        """Method removes randomly cargo card from ship's hold, most often hitting the hold."""
        cargo_cards = []
        for i in range(1, 9):
            if getattr(self, f"cargo_card_{i}"):
                cargo_cards.append(getattr(self, f"cargo_card_{i}"))
                setattr(self, f"cargo_card_{i}", None)
        index_to_remove = random.randrange(len(cargo_cards))
        cargo_cards.pop(index_to_remove)
        for index, card in enumerate(cargo_cards):
            setattr(self, f"cargo_card_{index + 1}", card)
        self.save()

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
