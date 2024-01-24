from django.db import models
from .game import Game
from dataset.models import GloryCard


class PlayersGloryCards(models.Model):
    """Presents a Players Glory Cards for game."""

    COLOURS = [
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
    ]

    @classmethod
    def set_values_default(cls):
        fields = cls.objects.all()
        for field in fields:
            field.game_round = 0
            field.glory_card_1 = None
            field.glory_card_2 = None
            field.glory_card_3 = None
            field.glory_card_4 = None
            field.glory_card_5 = None
            field.glory_card_6 = None
            field.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)
    player_colour = models.CharField(max_length=20, null=True, blank=True, choices=COLOURS)

    glory_card_1 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_1')
    glory_card_2 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_2')
    glory_card_3 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_3')
    glory_card_4 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_4')
    glory_card_5 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_5')
    glory_card_6 = models.ForeignKey(GloryCard, on_delete=models.CASCADE, null=True, blank=True, related_name='glory_card_6')

    def __str__(self):
        return f"Player Glory Card."
