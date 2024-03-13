from django.db import models
from dataset.utils.dataset.decorators.choices import PLAYER_COLOURS
from game.models import Game


class NavBarGame(models.Model):
    """A model that saves the current navigation state for the player."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields in model "gameNav"."""
        fields = cls._meta.get_fields()
        for field in fields:
            if field.name not in ['game_number', 'player_colour']:
                setattr(cls, field.name, False)
        cls.save()

    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    player_colour = models.CharField(max_length=30, null=True, blank=True, choices=PLAYER_COLOURS)

    move = models.BooleanField(default=False)
    to_port = models.BooleanField(default=False)
    from_port = models.BooleanField(default=False)
    to_sea_zone = models.BooleanField(default=False)
    n_direction = models.BooleanField(default=False)
    ne_direction = models.BooleanField(default=False)
    e_direction = models.BooleanField(default=False)
    se_direction = models.BooleanField(default=False)
    s_direction = models.BooleanField(default=False)
    sw_direction = models.BooleanField(default=False)
    w_direction = models.BooleanField(default=False)
    nw_direction = models.BooleanField(default=False)
    scout = models.BooleanField(default=False)
    merchant = models.BooleanField(default=False)
    merchant_raid = models.BooleanField(default=False)
    merchant_trade = models.BooleanField(default=False)
    merchant_escort = models.BooleanField(default=False)
    dutch_ship = models.BooleanField(default=False)
    english_ship = models.BooleanField(default=False)
    french_ship = models.BooleanField(default=False)
    spanish_ship = models.BooleanField(default=False)
    small_pirate_ship = models.BooleanField(default=False)
    large_pirate_ship = models.BooleanField(default=False)
    blue_player_ship = models.BooleanField(default=False)
    green_player_ship = models.BooleanField(default=False)
    red_player_ship = models.BooleanField(default=False)
    yellow_player_ship = models.BooleanField(default=False)
    port = models.BooleanField(default=False)
    sell_goods = models.BooleanField(default=False)
    but_goods = models.BooleanField(default=False)
    visit_shipyard = models.BooleanField(default=False)
    sell_buy_ship = models.BooleanField(default=False)
    buy_special_weapon = models.BooleanField(default=False)
    repair = models.BooleanField(default=False)
    buy_ship_modification = models.BooleanField(default=False)
    recruit = models.BooleanField(default=False)
    acquire_a_rumor = models.BooleanField(default=False)
    claim_a_mission = models.BooleanField(default=False)
    stash_gold = models.BooleanField(default=False)
    gain_loyality = models.BooleanField(default=False)
    get_favour = models.BooleanField(default=False)
    fishing = models.BooleanField(default=False)
    visit_location = models.BooleanField(default=False)

    back_to_port = models.BooleanField(default=False)
    back = models.BooleanField(default=False)
    end_turn = models.BooleanField(default=False)


    def __str__(self):
        return f"Player Nav Button State."
