import json
import random
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from dataset.utils.dataset.decorators.choices import COLOUR, HITS, HIT_LOCATIONS, PLAYER_COLOURS
from dataset.models import CargoCard
from dataset.models import MerchantTokens
from game.models import Game
from game.models import ShipsLocalisations
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import StackPlayerCargoCards
from game.models import TrackMerchantTokens
from game.models import TrackPlayerBounties
from game.models import TrackPlayerGolds
from game.models import TrackPlayerHitLocations
from game.models import TrackPlayerSpecialWeapons
from game.models import TrackGloryPoint
from game.serializers import CargoCardSerializer


@csrf_exempt
def navScoutActions(request):
    """Function is responsible for Scout Merchant."""


    data = {}
    game = Game.objects.get(number=100)
    ships_in_zone = ShipsLocalisations.objects.get(game_number=game)
    player_colour = request.session['playerColourActive']
    data['playerColour'] = player_colour
    player_localisation = getattr(ships_in_zone, f"{player_colour}_ship")
    merchants_track = TrackMerchantTokens.objects.get(game_number=game)
    player_captain_card = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_golds = TrackPlayerGolds.objects.get(game_number=game)
    player_bounties_instance = TrackPlayerBounties.objects.get(game_number=game)
    player_special_weapons_instance = TrackPlayerSpecialWeapons.objects.get(game_number=game)
    player_hits_locations_instance = TrackPlayerHitLocations.objects.get(player_colour=player_colour)
    player_ship = getattr(PlayersShipsCards, f"player_{player_colour}")
    player_cargo_cards = StackPlayerCargoCards.objects.get(player_colour=player_colour)


    # GET ALL SHIPS IN SEA ZONE where the scouting will be (without actual player)
    if request.GET.get('when') == 'scout':
        ships = [field.name for field in ships_in_zone._meta.get_fields() if not field.is_relation and 'ship' in field.name.lower()]
        ships_values = {field_name: getattr(ships_in_zone, field_name) for field_name in ships}
        for ship in ships_values.keys():
            if f"{player_colour}_ship" == ship: # actual player
                continue
            elif ships_values[ship] == player_localisation and any([colour[0].lower() in ship for colour in PLAYER_COLOURS]): # other player
                if not getattr(ships_in_zone, ship.replace('_ship', '_in_port')):
                    data[f"{ship.replace('_ship', 'PlayerShip')}"] = True
            elif ships_values[ship] == player_localisation and any([colour[0].lower().replace(' ', '_') in ship for colour in COLOUR]): # other NPC
                data[f"{ship.replace('_pirate', 'Pirate').replace('_ship', 'Ship')}"] = True
            elif ship == 'merchants_ship': # merchants
                if player_localisation in ships_values['merchants_ship']: # merchant is in sea zone with player
                    data['merchantToken'] = True


    # Merchant - Raid, Trade, Escort
    if request.GET.get('when') == 'merchant':
        # if any location is destroyed you cannot interact with merchant
        for hit_localisation in HIT_LOCATIONS:
            if getattr(player_hits_locations_instance, hit_localisation) == 0:
                data['playerHaveDestroyedHitLocation'] = True
                break
        # if player is Pirate (have min. 1 Bounty)
        if len(getattr(player_bounties_instance, f"player_{player_colour}")) != 0:
            data['playerIsPirate'] = True

    return JsonResponse(data)
