from django.db import models
from dataset.utils.dataset.decorators.choices import COLOUR, DISPOSABLE_ACTIONS, HIT_LOCATIONS, PLAYER_COLOURS
from game.models import Game
from game.models import PlayersCaptainsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import TrackPlayerBounties
from game.models import TrackPlayerHitLocations


class NavBarGame(models.Model):
    """A model that saves the current navigation state for the player."""

    @classmethod
    def set_default_values(cls):
        """Setting defaults values for all fields "navBarGame" after START GAME."""
        fields = cls.objects.all()
        for field in fields:
            field.player_blue = list()
            field.player_green = list()
            field.player_red = list()
            field.player_yellow = list()
            # field.player_yellow.append("Chain Shot")
            field.save()

    def player_nav(self, colour: str, *disposables: str, start=False):
        """
        Nav setting for player after drawing Event Card.
        Automatic saving.

        Arguments:
        colour: 'blue', 'green', 'red', 'yellow'.
        disposables: for one-time actions in one one round.
        start: True when player starts his turn.
        
        """

        # instances
        game = Game.objects.get(number=100) # game instance
        bounties = TrackPlayerBounties.objects.get(game_number=game) # bounties instance
        missions = StackMissionsCards.objects.get(game_number=game) # missions instance
        game_captains = PlayersCaptainsCards.objects.get(game_number=game)
        captain = getattr(game_captains, f"player_{colour}") # player Captain
        player_hits_locations = TrackPlayerHitLocations.objects.get(player_colour=colour) # hit locations on player board
        ship_localisations = ShipsLocalisations.objects.get(game_number=game) # ship localisations instance
        player_localisation = getattr(ship_localisations, f"{colour}_ship") # actual player localisation (name Sea Zone)

        # player_list = list(getattr(self, f"player_{colour}")) # field for player (list in JSON - as below)
        if start: # when player start his turn
            player_list = list() # field for player (list in JSON - as below)
        else: # during player turn, between actions
            actual_player_list = list(getattr(self, f"player_{colour}"))
            player_list = [action for action in actual_player_list if action in DISPOSABLE_ACTIONS]

            # IF PLAYER IN PORT
            if getattr(ship_localisations, f"{colour}_in_port"):
                # if inPort (for moves and port actions)
                player_list.append('playerInPort')
                # if "mission" is available (for Claim Mission)
                for mission_card in ['mission_1_card', 'mission_2_card', 'mission_3_card']:
                    if getattr(missions, mission_card) and (getattr(missions, mission_card)).port == player_localisation:
                        player_list.append('missionInPort')
                # if HomePort (for Stash Gold)
                if captain.home_port == player_localisation:
                    player_list.append('captainHomePort')
            else: # IF PLAYER IS OUT PORT
                # location
                player_list.append('visitLocation')
                # scout
                # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
                ships = [field.name for field in ship_localisations._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
                ships_values = {field_name: getattr(ship_localisations, field_name) for field_name in ships}
                for ship in ships_values.keys():

                    if f"{colour}_ship" == ship: # actual player
                        continue

                    if ships_values[ship] == player_localisation and any([col[0].lower() in ship for col in PLAYER_COLOURS]): # other player
                        if not getattr(ship_localisations, ship.replace('_ship', '_in_port')):
                            player_list.append(f"{ship.replace('_ship', 'PlayerShip')}")
                            # data[f"{ship.replace('_ship', 'PlayerShip')}"] = True

                    if ships_values[ship] == player_localisation and any([colour[0].lower().replace(' ', '_') in ship for colour in COLOUR]): # other NPC
                        player_list.append(f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}")
                        # data[f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}"] = True

                    if ship == 'merchants_ship': # merchants
                        if player_localisation in ships_values['merchants_ship']: # merchant is in sea zone with player
                            player_list.append('merchantToken')
                            # data['merchantToken'] = True

                # if any location is destroyed you cannot interact with merchant (raid and escort merchant)
                for hit_location in HIT_LOCATIONS:
                    if getattr(player_hits_locations, hit_location) == 0:
                        player_list.append('playerHaveDestroyedHitLocation')
                        break

                # if player has any Bounty - player is Pirate, they cannot trade with merchant (trade merchant)
                if len(getattr(bounties, f"player_{colour}")) != 0:
                    player_list.append('playerIsPirate')


            # player in "The Caribbean Sea"? (for moves actions)
            if player_localisation == 'The Caribbean Sea':
                player_list.append('isInTheCaribbeanSea')

            for disposable in disposables:
                player_list.append(disposable)

        setattr(self, f"player_{colour}", player_list)
        self.save()


    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)

    player_blue = models.JSONField(default=list, null=True, blank=True)
    player_green = models.JSONField(default=list, null=True, blank=True)
    player_red = models.JSONField(default=list, null=True, blank=True)
    player_yellow = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"Player Nav Button State."
