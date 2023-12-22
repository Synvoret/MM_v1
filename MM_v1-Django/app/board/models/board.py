from django.db import models
from game.models import Game


class Board(models.Model):
    """Game board database. All tracks, cards stacks."""

    class Meta:
        verbose_name = 'Board'

    name = models.CharField(max_length=150, default='Board Game')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    board = models.ImageField(upload_to='board/' ,null=True, blank=True)

    def __str__(self):
        return f"Board for game nr. {self.game.number}"
