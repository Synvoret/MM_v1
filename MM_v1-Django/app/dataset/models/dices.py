from django.db import models


class Dice(models.Model):
    """Dices for game."""

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dices/', blank=True, null=True)
    value = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Dice - {self.name}"

    @classmethod
    def get_dice(cls, name):
        """Method return image url for many dices."""
        dice = cls.objects.filter(name=name)
        return dice

    @classmethod
    def dice_comparison(cls, first_dices: list, second_dices: list):
        """
        Comparison return of result tests for two sets.
        - True if first_dices wins
        - False if first_dices lose
        - None if no success or draw
        """
        count_first_dices_skulls = sum(1 for result in first_dices if result == 'skull')
        count_second_dices_skulls = len([result for result in second_dices if result == 'skull'])
        sum_first_dices_numbers = sum(int(result) for result in first_dices if result != 'skull')
        sum_second_dices_numbers = sum(int(result) for result in second_dices if result != 'skull')
        if count_first_dices_skulls == 0 and count_second_dices_skulls == 0: # no success, draw
            return 'no success'
        elif count_first_dices_skulls > count_second_dices_skulls:
            return 'winner'
        elif count_first_dices_skulls < count_second_dices_skulls:
            return 'loser'
        elif count_first_dices_skulls == count_second_dices_skulls:
            if sum_first_dices_numbers > sum_second_dices_numbers:
                return 'winner'
            elif sum_first_dices_numbers < sum_second_dices_numbers:
                return 'loser'
            elif sum_first_dices_numbers == sum_second_dices_numbers: # draw
                return 'draw'
