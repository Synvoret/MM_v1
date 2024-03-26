import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataset.utils.dataset.decorators.choices import COLOUR, HIT_LOCATIONS, LOYALITY, PLAYER_COLOURS, SPECIALWEAPONS, UNITS
from dataset.models import CargoCard
from dataset.models import ShipCard
from dataset.models import CommandBoatCard
from dataset.models import SupportBoatCard
from dataset.models import Cube
from dataset.models import ShipModifications
from dataset.models import SpecialWeapon
from game.models import Game
from game.models import GameDemandTokens
from game.models import GameShipModifications
from game.models import PlayersCaptainsCards
from game.models import PlayersShipsCards
from game.models import ShipsLocalisations
from game.models import StackMissionsCards
from game.models import StackPlayerCargoCards
from game.models import TrackFavors
from game.models import TrackGloryPoint
from game.models import TrackLoyality
from game.models import TrackPlayerGolds
from game.models import TrackPlayerHitLocations
from game.models import TrackPlayerSpecialWeapons
from game.models import TrackPlayersShipModifications
from game.serializers import CargoCardSerializer
from nav.models import NavBarGame


@csrf_exempt
def portAction(request):
    """Function is responsible for Port Actions."""

    data = {}
    game = Game.objects.get(number=100)
    player_colour = request.session['playerColourActive']
    demand_tokens = GameDemandTokens.objects.get(game_number=game)
    missions_stack = StackMissionsCards.objects.get(game_number=game)
    player_golds = TrackPlayerGolds.objects.get(game_number=game)
    player_captain_instance = getattr(PlayersCaptainsCards, f"player_{player_colour}")
    player_ship = PlayersShipsCards.objects.get(game_number=game)
    player_cargo_cards_instance = StackPlayerCargoCards.objects.get(player_colour=player_colour)
    player_hit_locations = TrackPlayerHitLocations.objects.get(player_colour=player_colour)
    ship_localisations = ShipsLocalisations.objects.get(game_number=game)
    player_special_weapons = TrackPlayerSpecialWeapons.objects.get(game_number=game)
    player_modifications = TrackPlayersShipModifications.objects.get(game_number=game)
    port_modifications = GameShipModifications.objects.get(game_number=game)
    favours = TrackFavors.objects.get(game_number=game)
    loyality = TrackLoyality.objects.get(game_number=game)
    nav_bar = NavBarGame.objects.get(game_number=game)
    player_nav_bar = getattr(nav_bar, f"player_{player_colour}")


    # GET method
    if request.method == 'GET':


        # port


        # sell goods (always as first, only one time in turn)
        if request.GET.get('type_request') == 'sell goods':
            for i in range(1, 9):
                if getattr(player_cargo_cards_instance, f"cargo_card_{i}"):
                    card = getattr(player_cargo_cards_instance, f"cargo_card_{i}")
                    data[f"playerCargo{i}"] = card.cargo
                    data[f"playerCargoCard{i}ImageUrl"] = card.awers.url
                else: 
                    break
            port_name = str(getattr(ship_localisations, f"{player_colour}_ship")).lower().replace(' ', '_')
            demand_token_in_port = getattr(demand_tokens, port_name)
            data['demanTokenInPort'] = demand_token_in_port.cargo
            data['demanTokenInPortImageUrl'] = demand_token_in_port.awers.url


        if request.GET.get('type_request') == 'buy goods':
            cargo_cards = CargoCard.objects.all() # drawing 6 cards in standard
            port_name = str(getattr(ship_localisations, f"{player_colour}_ship")).lower().replace(' ', '_')
            demand_token_in_port = getattr(demand_tokens, port_name)
            data['playerGolds'] = getattr(player_golds, f"player_{player_colour}")
            amount_cargo = 6
            # cargo for buy
            for i in range(1, amount_cargo + 1):
                while True: # randomly card, other as demand token in port
                    cargo_card = random.choice(cargo_cards)
                    if cargo_card.cargo == demand_token_in_port.cargo:
                        continue
                    else:
                        serializer = CargoCardSerializer(cargo_card)
                        request.session[f"cargoCard{i}ToBuy"] = serializer.data
                        data[f"cargoCard{i}ToBuy"] = request.session[f"cargoCard{i}ToBuy"]
                        break
            # player cargo cards and free space in ship cargo
            ship_hold = player_hit_locations.cargo
            for i in range(1, 9): # player cargo cads
                if getattr(player_cargo_cards_instance, f"cargo_card_{i}"):
                    serializer = CargoCardSerializer(getattr(player_cargo_cards_instance, f"cargo_card_{i}"))
                    request.session[f"playerCargoCard{i}"] = serializer.data
                    data[f"playerCargoCard{i}"] = request.session[f"playerCargoCard{i}"]
                    ship_hold -= 1
                else:
                    break
            data['freeSpaceInShipHold'] = ship_hold


        if request.GET.get('type_request') == 'ship':
            data['playerGolds'] = player_golds.golds_amount(player_colour)


        if request.GET.get('type_request') == 'ship sell buy':
            player = getattr(player_ship, f"player_{player_colour}")
            for unit in UNITS:
                if unit.lower().replace(' ', '-') in request.GET.get('unitID'):
                    if unit == 'Command Boat':
                        data['unitBuy'] = 5
                        data['unitSell'] = 2
                    elif unit == 'Support Boat':
                        data['unitBuy'] = 3
                        data['unitSell'] = 1
                    else:
                        ship = ShipCard.objects.get(ship=unit, ship_type=3)
                        data['unitBuyCost'] = ship.buy_cost
                        data['unitSellCost'] = player.sell_cost
                        data['unitBuyShip'] = ship.ship
                        data['unitSellShip'] = player.ship
                        amount_dameges = player_hit_locations.amount_damages(f"player_{player_colour}")
                        data['damagesPlayerUnit'] = amount_dameges
                        amount_modifications = player_modifications.amount_modifications(player_colour)
                        data['modificationsPlayerUnit'] = amount_modifications

            data[f"playerShipImageUrl"] = player.awers.url


        # visit shipyard special weapon
        if request.GET.get('type_request') == 'special weapon':
            data['playerGolds'] = player_golds.golds_amount(player_colour)
            # weapons for sell and for buy
            player_weapons = getattr(player_special_weapons, f"player_{player_colour}")
            for special_weapon in SPECIALWEAPONS:
                if special_weapon in player_weapons:
                    data[f"forSell{special_weapon.replace(' ', '')}"] = (SpecialWeapon.objects.get(name=special_weapon)).image.url
                    continue
                else:
                    data[f"forBuy{special_weapon.replace(' ', '')}"] = (SpecialWeapon.objects.get(name=special_weapon)).image.url


        # visit shipyard Repair ship's locations
        if request.GET.get('type_request') == 'repair':
            data['playerGolds'] = player_golds.golds_amount(player_colour)
            for hit_location in HIT_LOCATIONS:
                data[f"player{hit_location.capitalize()}Value"] = player_hit_locations.value_location(hit_location)
                data[f"player{hit_location.capitalize()}MaxValue"] = player_hit_locations.max_value_location(f"player_{player_colour}", hit_location)

            data['playerCubeImageUrl'] = Cube.player_cube(player_colour)
            data['playerCubeMaxImageUrl'] = Cube.player_cube_max(player_colour)


        if request.GET.get('type_request') == 'modifications':
            data['playerGolds'] = player_golds.golds_amount(player_colour)
            player_modifications = getattr(player_modifications, f"player_{player_colour}")
            # modification to buy in port
            port = (getattr(ship_localisations, f"{player_colour}_ship")).lower().replace(' ', '_').replace('-', '_')
            port_modification = getattr(port_modifications, port)
            try: 
                data['forBuy'] = ShipModifications.objects.get(name=port_modification).awers.url
                data['portModification'] = port_modification
            except: 
                pass
            finally:
                data['tokenFlip'] = port.replace('_', '-')
            # player modifications
            for index, player_modification in enumerate(player_modifications):
                data[f"forSell{player_modification}"] = (ShipModifications.objects.get(name=player_modification)).awers.url


    # POST method
    if request.method == 'POST':


        # accept sold goods
        if request.POST.get('type_request') == 'sell goods accept':
            port = str(getattr(ship_localisations, f"{request.session['playerColourActive']}_ship"))
            data['port'] = port.lower().replace(' ', '-')
            list_numbers = list(json.loads(request.POST.get('numbers'))) # sold goods

            # update cargo cards
            for number in list_numbers:
                setattr(player_cargo_cards_instance, f"cargo_card_{number}", None)
                player_cargo_cards_instance.save()
                try: del request.session[f"playerCargoCard{number}"]
                except: pass
            player_goods = []
            for i in range(1, 9): # making new player goods list
                player_goods.append(getattr(player_cargo_cards_instance, f"cargo_card_{i}"))
                setattr(player_cargo_cards_instance, f"cargo_card_{i}", None) # clear db
            player_goods_new_queue = [cargo for cargo in player_goods if cargo is not None]
            for index, cargo in enumerate(player_goods_new_queue):
                setattr(player_cargo_cards_instance, f"cargo_card_{index + 1}", cargo) # add left goods to db
            player_cargo_cards_instance.save()

            # update golds
            if int(request.POST.get('golds')) != 0:
                player_golds.increase_golds(f"player_{player_colour}", int(request.POST.get('golds')))

            # update glory
            if int(request.POST.get('glory')) == 1:
                glory_points_track_instance = TrackGloryPoint.objects.get(game_number=game)
                glory_points_track_instance.increase_glory_point(f"player_{player_colour}")

            # update navBarGame
            nav_bar.player_nav(player_colour, 'sellGoods')


        # accept bought goods
        if request.POST.get('type_request') == 'buy goods accept':

            list_numbers = list(json.loads(request.POST.get('numbers'))) # bought goods

            # update cargo cards
            for number in list_numbers: # id for cargo cards
                player_cargo_cards_instance.add_cargo_card(number)

            # cleaning request.session
            keys_to_remove = []
            for key in request.session.keys():
                if "Card" in key:
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                del request.session[key]

            # update golds
            if int(request.POST.get('golds')) != 0:
                player_golds.change_golds(f"player_{player_colour}", int(request.POST.get('golds')))

            # update navBarGame
            nav_bar.player_nav(player_colour, 'buyGoods')
            print(dict(request.session))


        if request.POST.get('type_request') == 'ship sell buy accept':
            print(request.POST.get('newUnit'), type(request.POST.get('newUnit')))
            print(request.POST.get('profitForSell'), type(request.POST.get('profitForSell')))
            print(request.POST.get('costForBuy'), type(request.POST.get('costForBuy')))
            print('zapisuje zakupy statku')


        if request.POST.get('type_request') == 'special weapon buy' or request.POST.get('type_request') == 'special weapon sell':
            selected_weapon = str(request.POST.get('weapon')).replace('-', ' ').title()
            if request.POST.get('type_request') == 'special weapon sell':
                player_special_weapons.remove_weapon(f"player_{player_colour}", selected_weapon)
                player_golds.increase_golds(f"player_{player_colour}", 1)
            if request.POST.get('type_request') == 'special weapon buy' and player_golds.decrease_golds(f"player_{player_colour}", 3):
                player_special_weapons.add_weapon(f"player_{player_colour}", selected_weapon)


        # repair location hull, cargo, masts, cannons
        if 'repair location' in request.POST.get('type_request'):
            if player_golds.golds_amount(player_colour) >= 2:
                loaction = (str(request.POST.get('type_request')).split(' '))[-1]
                if player_hit_locations.repair_location(f"player_{player_colour}", loaction):
                    player_golds.decrease_golds(f"player_{player_colour}", 2)


        if request.POST.get('type_request') == 'modification buy' or request.POST.get('type_request') == 'modification sell':
            bought_modification = request.POST.get('modification')
            if request.POST.get('type_request') == 'modification buy':
                if player_modifications.add_modification(player_colour, bought_modification) and player_golds.decrease_golds(f"player_{player_colour}", 3):
                    setattr(port_modifications, (getattr(ship_localisations, f"{player_colour}_ship")).lower().replace(' ','_'), None)
                    port_modifications.save()
            if request.POST.get('type_request') == 'modification sell':
                player_modifications.remove_modification(player_colour, bought_modification)
                player_golds.increase_golds(f"player_{player_colour}", 1)


        # stash gold
        if request.POST.get('type_request') == 'stash gold':
            if getattr(player_golds, f"player_{player_colour}") > 0:
                loyality.decrease_loyality(f"player_{player_colour}")


        # raise loyality
        if request.POST.get('type_request') == 'raise loyality':

            player_loyality = getattr(loyality, f"player_{player_colour}")

            if 'raiseLoyality' in player_nav_bar or player_loyality == 'Fierce Loyality':
                data['cantChangeLoyality'] = True
            else:
                nav_bar.player_nav(player_colour, 'raiseLoyality')
                if getattr(player_golds, f"player_{player_colour}") >= 3:
                    if player_loyality == 'Happy':
                        player_golds.decrease_golds(f"player_{player_colour}", 3)
                    elif player_loyality == 'Pleased':
                        player_golds.decrease_golds(f"player_{player_colour}", 3)
                    elif player_loyality == 'Content':
                        player_golds.decrease_golds(f"player_{player_colour}", 3)
                    elif player_loyality == 'Restless':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                    elif player_loyality == 'Unhappy':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                    elif player_loyality == 'Angry':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                elif getattr(player_golds, f"player_{player_colour}") == 2:
                    if player_loyality == 'Restless':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                    elif player_loyality == 'Unhappy':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                    elif player_loyality == 'Angry':
                        player_golds.decrease_golds(f"player_{player_colour}", 2)
                loyality.increase_loyality(f"player_{player_colour}")


        # gain favour
        if request.POST.get('type_request') == 'get favour':
            if getattr(player_golds, f"player_{player_colour}") < 2:
                data['cantGetFavour'] = True
            else:
                nav_bar.player_nav(player_colour, 'getFavour')
                player_golds.decrease_golds(f"player_{player_colour}", 2)
                favours.increase_favour_point(f"player_{player_colour}")


    data['playerColour'] = player_colour
    return JsonResponse(data)
