from copy import deepcopy
from django.db import models
from dataset.utils.dataset.decorators.choices import BATTLEDECLARATIONS
from dataset.models import Dice
from dataset.models import ShipCard


class CombatFlow(models.Model):
    """Combat Flow History."""

    combat = models.JSONField(default=list, blank=True, null=True)

    def first_round(self, defender_ship: str):
        self.__class__.objects.all().delete()
        aggressor_ship_stat = ShipCard.objects.filter(ship='Frigate').first() # random ship for now
        # defender_ship_stat = ShipCard.objects.filter(ship=defender_ship).first()
        defender_ship_stat = ShipCard.objects.filter(ship='Frigate').first()
        record = {
            "round": 1,
            "dice1Image": Dice.objects.get(name='one').image.url,
            "aggressor": {
                "ship": aggressor_ship_stat.ship,
                "hull": aggressor_ship_stat.toughness,
                "cargo": aggressor_ship_stat.cargo,
                "masts": aggressor_ship_stat.toughness,
                "crew": aggressor_ship_stat.crew,
                "cannons": aggressor_ship_stat.cannons,
                "maneuverability": aggressor_ship_stat.maneuverability,
                # 'seamanship': 8,
                'seamanship': 1,
                'leadership': 1,
                'special_weapons': ['Hook'],
                'ship_modifications': [],
                'declaration': '',
                'seamanship_roll_result': [],
                'seamanship_result_comparison': None,
                'shot_roll_result': [],
                'board_roll_result': [],
                "actions": [],
            },
            "defender": {
                "ship": defender_ship_stat.ship,
                "hull": defender_ship_stat.toughness,
                "cargo": defender_ship_stat.cargo,
                "masts": defender_ship_stat.toughness,
                "crew": defender_ship_stat.crew,
                "cannons": defender_ship_stat.cannons,
                "maneuverability": defender_ship_stat.maneuverability,
                # 'seamanship': 8,
                'seamanship': 1,
                'leadership': 1,
                'special_weapons': ['Grape', 'Hook', 'Chains'],
                'ship_modifications': [],
                'declaration': '',
                'seamanship_roll_result': [],
                'seamanship_result_comparison': None,
                'shot_roll_result': [],
                'board_roll_result': [],
                "actions": [],
            },
        }
        self.combat = []
        self.combat.append(record)
        self.save()


    def update_round_record(self, side: str, parameter, value):
        # roll seamanship dices, parameter = 'seamanship'
        if parameter in ['shot', 'board', 'seamanship']:
            self.combat[-1][side][f'{parameter}_roll_result'].append(value)
        # after choosen declaration, parameter = 'declaration'
        if parameter == 'declaration':
            self.combat[-1][side][parameter] = value
        # after choosen actions, parameter = 'actions'
        if parameter == 'actions':
            self.combat[-1][side][parameter] = value
        if parameter == 'seamanship_result':
            self.combat[-1][side]['seamanship_result_comparison'] = value
        if parameter in ['hull', 'cargo', 'masts', 'crew', 'cannons']:
            if side == 'aggressor':
                side = 'defender'
                print(f'MODYFIKUJĘ BAZĘ PO STRZALE Z DZIAŁ, aggresor strzela w {parameter} {side}a')
            elif side == 'defender':
                side = 'aggressor'
                print(f'MODYFIKUJĘ BAZĘ PO STRZALE Z DZIAŁ, defender strzela w {parameter} {side}a')

            if self.combat[-1][side][parameter] > 0:
                self.combat[-1][side][parameter] -= 1
            elif self.combat[-1][side][parameter] == 0:
                self.combat[-1][side]['hull'] -= 1

        self.save()

    def next_round(self):
        last_round = self.combat[-1]
        new_round = deepcopy(last_round)
        new_round['round'] = last_round['round'] + 1
        new_round['aggressor']['declaration'] = ''
        new_round['defender']['declaration'] = ''
        new_round['aggressor']['seamanship_roll_result'] = []
        new_round['defender']['seamanship_roll_result'] = []
        new_round['aggressor']['seamanship_result_comparison'] = None
        new_round['defender']['seamanship_result_comparison'] = None
        new_round['aggressor']['shot_roll_result'] = []
        new_round['defender']['shot_roll_result'] = []
        new_round['aggressor']['board_roll_result'] = []
        new_round['defender']['board_roll_result'] = []
        new_round['aggressor']['actions'] = []
        new_round['defender']['actions'] = []
        self.combat.append(new_round)
        self.save(update_fields=['combat'])

    def __str__(self):
        return f"Combat Flow History."
